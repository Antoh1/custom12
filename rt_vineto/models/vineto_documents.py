# -*- coding: utf-8 -*-

from datetime import timedelta

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError


class QuoteSettings(models.Model):
    _name = 'document.defaults'
    _description = 'Document Defaults'
    #_rec_name = 'note'

    name = fields.Char(string="Title", store=True, copy=True)
    note = fields.Html(string='Note | Terms', store=True, copy=True)
    payment_details = fields.Html(string='Payment Details', store=True, copy=True)
    details = fields.Html('Payment Details', sanitize_style=True)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    machine = fields.Char(string="Machine Type", store=True)
    customer_ref = fields.Char(string="REF", store=True)
    customer_rep = fields.Char(string="Attention", store=True)
    lpo_number = fields.Char(string="LPO Number", store=True)
    payment_details = fields.Html(compute='_get_defaults', string="Payment Details")
    payment_condition = fields.Html(compute='_get_defaults', string='Terms of Payment')
    details = fields.Html(compute='_get_defaults', sttring='Bank Details', sanitize_style=True)

    @api.multi
    def _get_defaults(self):
        quote_defaults = self.env['document.defaults'].search([('id', '=', 1)])
        self.payment_details = quote_defaults.payment_details
        self.payment_condition = quote_defaults.note
        self.details = quote_defaults.details


    # @api.multi
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         if 'company_id' in vals:
    #             vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('vineto.sale.order.code') or _('New')
    #         else:
    #             vals['name'] = self.env['ir.sequence'].next_by_code('vineto.sale.order.code') or _('New')
    #     record = super(SaleOrder, self).create(vals)
    #     return record


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    # is_project_invoice = fields.Boolean(string="Is Project Invoice")
    delivery_note = fields.Char(compute='_get_delivery', string="Delivery Note", help="Source Document")
    # sale_id = fields.Many2one('sale.order', string='Sale Order')
    lpo_number = fields.Char(compute='_get_delivery', string="LPO Number")
    details = fields.Html(compute='_get_defaults', string="Payment Details")
    payment_condition = fields.Html(compute='_get_defaults', string='Terms of Payment')

    @api.multi
    def _get_defaults(self):
        quote_defaults = self.env['document.defaults'].search([('id', '=', 1)])
        self.details = quote_defaults.details
        self.payment_condition = quote_defaults.note

    @api.multi
    def _get_delivery(self):
        delivery_slips = self.env['stock.picking'].search([('origin', '=', self.origin)])
        self.delivery_note = ""
        for delivery in delivery_slips:
            if len(delivery_slips)>1:
                self.delivery_note = delivery.name
                self.lpo_number = delivery.sale_id.lpo_number
            else:
                self.delivery_note = self.delivery_note + "|" + delivery.name
                self.lpo_number = delivery.sale_id.lpo_number

    # @api.multi
    # def _get_lpo(self):
    #     invoices = self.env['account.invoice'].search([('type', '=', 'out_invoice')])
    #     sale_orders = self.env['sale.order'].search([])
    #     for inv in invoices:
    #         for o in sale_orders:
    #             inv.lpo_number = o.lpo_number



class DeliveryVehicle(models.Model):
    _name = 'delivery.vehicle'
    _description = 'Delivery Vehicle'

    name = fields.Char(string="Vehicle Type")
    vehicle_no = fields.Char(string="Vehicle Registration")
    driver = fields.Char(string="Driver")
    driver_no = fields.Char(string="Driver Contact")


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    vehicle = fields.Many2one("delivery.vehicle")
    vehicle_no = fields.Char(related="vehicle.vehicle_no")
    lpo_number = fields.Char(compute='_get_lpo', string="LPO Number")
    driver = fields.Char(related="vehicle.driver")
    driver_no = fields.Char(related="vehicle.driver_no")
    invoice_no = fields.Char(compute='_get_invoice', string="Invoice No", help="Source Document")

    @api.multi
    def _get_invoice(self):
        invoice_slips = self.env['account.invoice'].search([('origin', '=', self.origin)])
        self.invoice_no = invoice_slips.number

    @api.multi
    def _get_lpo(self):
        delivery_slips = self.env['stock.picking'].search([('origin', '=', self.origin)])
        self.lpo_number = delivery_slips.sale_id.lpo_number
