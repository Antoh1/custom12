from datetime import date, datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProjectProduct(models.Model):
    _inherit = 'product.template'

    is_m2 = fields.Boolean(string="sold in SQM?")
    sqm_measures = fields.One2many('sqm.measurement', 'product_id', string='SQM Measurements', store=True)
