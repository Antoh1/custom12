import logging

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
from odoo.osv import expression

from odoo.addons import decimal_precision as dp


_logger = logging.getLogger(__name__)


class ProjectQuoteInvoices(models.Model):
    _inherit = 'sale.order'

    quote_note = fields.Text(string="Details")
    payment_details = fields.Text(compute='_get_defaults', string="Payment Details")
    payment_condition = fields.Text(compute='_get_defaults', string='Terms of Payment')

    @api.multi
    def _get_defaults(self):
        quote_defaults = self.env['quote.defaults'].search([('id', '=', 1)])
        self.payment_details = quote_defaults.payment_details
        self.payment_condition = quote_defaults.note


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
    driver = fields.Char(related="vehicle.driver")
    driver_no = fields.Char(related="vehicle.driver_no")

