from datetime import date, datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProjectProduct(models.Model):
    _name = 'sqm.measurement'

    length = fields.Integer(string="Length")
    width = fields.Integer(string="Width")
    quantity = fields.Integer(string="Quantity")
    product_id = fields.Many2one('product.product')
