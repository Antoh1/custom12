# -*- coding: utf-8 -*-

import logging
import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
from odoo.osv import expression
from collections import defaultdict
from odoo.exceptions import UserError
from odoo.tools import float_compare, float_round, float_is_zero, pycompat

from odoo.addons import decimal_precision as dp

from odoo.tools import float_compare, pycompat

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
	#_name = 'product.template'
    _inherit = 'product.template'

    oe_number = fields.Char('Part Number')
    v_number = fields.Char('Vendor Number')
    default_code = fields.Char('Brand')
    show_part_number = fields.Boolean('Print Part Number?', default=True)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # oe_number = fields.Char('OE Number')
    # v_number = fields.Char('Vendor Number')
    # default_code = fields.Char('Brand')

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        if not args:
            args = []
        if name:
            positive_operators = ['=', 'ilike', '=ilike', 'like', '=like']
            product_ids = []
            if operator in positive_operators:
                product_ids = self._search([('default_code', '=', name)] + args, limit=limit,
                                           access_rights_uid=name_get_uid)
                if not product_ids:
                    product_ids = self._search([('barcode', '=', name)] + args, limit=limit,
                                               access_rights_uid=name_get_uid)
            if not product_ids and operator not in expression.NEGATIVE_TERM_OPERATORS:
                # Do not merge the 2 next lines into one single search, SQL search performance would be abysmal
                # on a database with thousands of matching products, due to the huge merge+unique needed for the
                # OR operator (and given the fact that the 'name' lookup results come from the ir.translation table
                # Performing a quick memory merge of ids in Python will give much better performance
                product_ids = self._search(args + ['|', '|', ('default_code', operator, name), ('oe_number', operator, name), ('v_number', operator, name)], limit=limit)
                if not limit or len(product_ids) < limit:
                    # we may underrun the limit because of dupes in the results, that's fine
                    limit2 = (limit - len(product_ids)) if limit else False
                    product2_ids = self._search(args + [('name', operator, name), ('id', 'not in', product_ids)],
                                                limit=limit2, access_rights_uid=name_get_uid)
                    product_ids.extend(product2_ids)
            elif not product_ids and operator in expression.NEGATIVE_TERM_OPERATORS:
                domain = expression.OR([
                    ['&', ('default_code', operator, name), ('name', operator, name)],
                    ['&', ('default_code', '=', False), ('name', operator, name)],
                ])
                domain = expression.AND([args, domain])
                product_ids = self._search(domain, limit=limit, access_rights_uid=name_get_uid)
            if not product_ids and operator in positive_operators:
                ptrn = re.compile('(\[(.*?)\])')
                res = ptrn.search(name)
                if res:
                    product_ids = self._search([('default_code', '=', res.group(2))] + args, limit=limit,
                                               access_rights_uid=name_get_uid)
            # still no results, partner in context: search on supplier info as last hope to find something
            if not product_ids and self._context.get('partner_id'):
                suppliers_ids = self.env['product.supplierinfo']._search([
                    ('name', '=', self._context.get('partner_id')),
                    '|',
                    ('product_code', operator, name),
                    ('product_name', operator, name)], access_rights_uid=name_get_uid)
                if suppliers_ids:
                    product_ids = self._search([('product_tmpl_id.seller_ids', 'in', suppliers_ids)], limit=limit,
                                               access_rights_uid=name_get_uid)
        else:
            product_ids = self._search(args, limit=limit, access_rights_uid=name_get_uid)
        return self.browse(product_ids).name_get()


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def get_sale_order_line_multiline_description_sale(self, product):
        if product.show_part_number:
            # return product.get_product_multiline_description_sale() +' | '+ product.oe_number
            return product.name +' | '+ product.oe_number
        else:
            # return product.get_product_multiline_description_sale()
            return product.name


# class StockMoveLine(models.Model):
#     inherit = 'stock.move.line'

# class StockMove(models.Model):
#     inherit = 'stock.move'
#     def _prepare_account_move_line(self, qty, cost, credit_account_id, debit_account_id):
#         """
#         Generate the account.move.line values to post to track the stock valuation difference due to the
#         processing of the given quant.
#         """
#         self.ensure_one()
#
#         if self._context.get('force_valuation_amount'):
#             valuation_amount = self._context.get('force_valuation_amount')
#         else:
#             valuation_amount = cost
#
#         # the standard_price of the product may be in another decimal precision, or not compatible with the coinage of
#         # the company currency... so we need to use round() before creating the accounting entries.
#         debit_value = self.company_id.currency_id.round(valuation_amount)
#
#         # check that all data is correct
#         # if self.company_id.currency_id.is_zero(debit_value) or self.env['ir.config_parameter'].sudo().get_param('stock_account.allow_zero_cost'):
#         #     raise UserError(_("The cost of %s is currently equal to 0. Change the cost or the configuration of your product to avoid an incorrect valuation.") % (self.product_id.display_name,))
#         credit_value = debit_value
#
#
#         valuation_partner_id = self._get_partner_id_for_valuation_lines()
#         res = [(0, 0, line_vals) for line_vals in self._generate_valuation_lines_data(valuation_partner_id, qty, debit_value, credit_value, debit_acc