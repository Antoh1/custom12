# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosOrder(models.Model):
    _inherit = 'pos.order'
    _description = 'Various Metrics for Pos Analysis'

    rt_payment_method = fields.Many2one(string="Payment Mode", related="statement_ids.journal_id")


class ProductTemplate(models.Model):
    _inherit = 'product.template'

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
