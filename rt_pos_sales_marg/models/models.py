# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'
    _order = "create_date desc"

    cost_price_id = fields.Float('Unit Cost', related='product_id.standard_price', groups=('point_of_sale.res_groups_64_25117fc4'))
    p_part_no = fields.Char('P No', related='product_id.oe_number', groups=('point_of_sale.res_groups_64_25117fc4'))
    pos_reference = fields.Char('Receipt Ref', related='order_id.pos_reference')
    cost_total = fields.Float(string='Total Cost', compute='_compute_total_cost', readonly=True, store=True)
    price_total = fields.Float(string='Total S.Price', compute='_compute_total_price', readonly=True, store=True)
    sale_pmargin = fields.Float(string='Sales Margin', compute='_compute_sales_margin', readonly=True, store=True)
    #partner_id = fields.Many2one('Customer', related='order_id.partner_id')
    #user_id = fields.Many2one('SalesPerson', related='order_id.user_id', store=True)

    @api.depends('cost_price_id', 'qty')
    def _compute_total_cost(self):
        for line in self:
            line.cost_total = line.cost_price_id * line.qty

    @api.depends('price_unit', 'qty')
    def _compute_total_price(self):
        for line in self:
            line.price_total = line.price_unit * line.qty

    @api.depends('cost_total', 'price_total')
    def _compute_sales_margin(self):
        for line in self:
            line.sale_pmargin = (line.price_total - line.cost_total)
