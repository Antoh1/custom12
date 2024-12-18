# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class MaterialUsed(models.Model):
    _name = 'material.used'
    _description = 'Item Description'
    _rec_name = 'item'

    item = fields.Many2one('item.group', string='Item(s)', required=True, copy=True)
    product_uom = fields.Many2one('quotation.uom', string='Unit(s)', required=True)
    items_used = fields.One2many('material.used.item', 'detail_id', string='Items Used', copy=True)
    items_quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
    items_rate = fields.Float(compute='_get_total', string="Rate", copy=True)
    items_total = fields.Float(compute='_get_total', string="Total", copy=True)
    # project_category = fields.Many2one(related='work_id.project_category', string="Project", required=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)
    work_id = fields.Many2one('planned.work', ondelete='cascade', domain="[('project_category', '=', project_category)]")
    work_idb = fields.Many2one('planned.workb', ondelete='cascade', domain="[('project_category', '=', project_category)]")
    work_idc = fields.Many2one('planned.workc', ondelete='cascade', domain="[('project_category', '=', project_category)]")
    work_idd = fields.Many2one('planned.workd', ondelete='cascade', domain="[('project_category', '=', project_category)]")
    work_ide = fields.Many2one('planned.worke', ondelete='cascade', domain="[('project_category', '=', project_category)]")
    work_idf = fields.Many2one('planned.workf', ondelete='cascade', domain="[('project_category', '=', project_category)]")
    work_idg = fields.Many2one('planned.workg', ondelete='cascade', domain="[('project_category', '=', project_category)]")
    work_idh = fields.Many2one('planned.workh', ondelete='cascade', domain="[('project_category', '=', project_category)]")
    work_idi = fields.Many2one('planned.worki', ondelete='cascade', domain="[('project_category', '=', project_category)]")
    work_idj = fields.Many2one('planned.workj', ondelete='cascade', domain="[('project_category', '=', project_category)]")
    #quote_id = fields.Many2one('project.quotation', ondelete='cascade', domain="[('project_category', '=', project_category)]")

    @api.multi
    def _get_total(self):
        for record in self:
            items_amount = 0
            items_qty = 0
            for item in record.items_used:
                items_amount += item.total
                items_qty += item.item_qty
            record.items_total = items_amount
            record.items_quantity = items_qty
            if items_qty == 0:
                items_qty = 1
            record.items_rate = round(items_amount / items_qty, 2)

    # @api.onchange('material')
    # def get_price(self):
    #     self.price = self.material.lst_price
    #     self.product_uom = self.material.uom_name


# class MaterialUsedB(models.Model):
#     _name = 'material.usedb'
#     _description = 'Item Description'
#     _rec_name = 'item'
#
#     item = fields.Many2one('item.group', string='Item(s)', required=True, copy=True)
#     product_uom = fields.Many2one('quotation.uom', string='Unit(s)', required=True)
#     items_used = fields.One2many('material.used.item', 'detail_id', string='Items Used', copy=True)
#     items_quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
#     items_rate = fields.Float(compute='_get_total', string="Rate", copy=True)
#     items_total = fields.Float(compute='_get_total', string="Total", copy=True)
#     project_category = fields.Many2one(related='work_id.project_category', string="Project", required=True)
#     work_id = fields.Many2one('planned.workb', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#     #quote_id = fields.Many2one('project.quotation', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#
#     @api.multi
#     def _get_total(self):
#         for record in self:
#             items_amount = 0
#             items_qty = 0
#             for item in record.items_used:
#                 items_amount += item.total
#                 items_qty += item.item_qty
#             record.items_total = items_amount
#             record.items_quantity = items_qty
#             if items_qty == 0:
#                 items_qty = 1
#             record.items_rate = round(items_amount / items_qty, 2)
#
#
# class MaterialUsedC(models.Model):
#     _name = 'material.usedc'
#     _description = 'Item Description'
#     _rec_name = 'item'
#
#     item = fields.Many2one('item.group', string='Item(s)', required=True, copy=True)
#     product_uom = fields.Many2one('quotation.uom', string='Unit(s)', required=True)
#     items_used = fields.One2many('material.used.item', 'detail_id', string='Items Used', copy=True)
#     items_quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
#     items_rate = fields.Float(compute='_get_total', string="Rate", copy=True)
#     items_total = fields.Float(compute='_get_total', string="Total", copy=True)
#     project_category = fields.Many2one(related='work_id.project_category', string="Project", required=True)
#     work_id = fields.Many2one('planned.workc', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#     #quote_id = fields.Many2one('project.quotation', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#
#     @api.multi
#     def _get_total(self):
#         for record in self:
#             items_amount = 0
#             items_qty = 0
#             for item in record.items_used:
#                 items_amount += item.total
#                 items_qty += item.item_qty
#             record.items_total = items_amount
#             record.items_quantity = items_qty
#             if items_qty == 0:
#                 items_qty = 1
#             record.items_rate = round(items_amount / items_qty, 2)
#
#
# class MaterialUsedD(models.Model):
#     _name = 'material.usedd'
#     _description = 'Item Description'
#     _rec_name = 'item'
#
#     item = fields.Many2one('item.group', string='Item(s)', required=True, copy=True)
#     product_uom = fields.Many2one('quotation.uom', string='Unit(s)', required=True)
#     items_used = fields.One2many('material.used.item', 'detail_id', string='Items Used', copy=True)
#     items_quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
#     items_rate = fields.Float(compute='_get_total', string="Rate", copy=True)
#     items_total = fields.Float(compute='_get_total', string="Total", copy=True)
#     project_category = fields.Many2one(related='work_id.project_category', string="Project", required=True)
#     work_id = fields.Many2one('planned.workd', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#     #quote_id = fields.Many2one('project.quotation', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#
#     @api.multi
#     def _get_total(self):
#         for record in self:
#             items_amount = 0
#             items_qty = 0
#             for item in record.items_used:
#                 items_amount += item.total
#                 items_qty += item.item_qty
#             record.items_total = items_amount
#             record.items_quantity = items_qty
#             if items_qty == 0:
#                 items_qty = 1
#             record.items_rate = round(items_amount / items_qty, 2)
#
#
# class MaterialUsedE(models.Model):
#     _name = 'material.usede'
#     _description = 'Item Description'
#     _rec_name = 'item'
#
#     item = fields.Many2one('item.group', string='Item(s)', required=True, copy=True)
#     product_uom = fields.Many2one('quotation.uom', string='Unit(s)', required=True)
#     items_used = fields.One2many('material.used.item', 'detail_id', string='Items Used', copy=True)
#     items_quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
#     items_rate = fields.Float(compute='_get_total', string="Rate", copy=True)
#     items_total = fields.Float(compute='_get_total', string="Total", copy=True)
#     project_category = fields.Many2one(related='work_id.project_category', string="Project", required=True)
#     work_id = fields.Many2one('planned.worke', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#     #quote_id = fields.Many2one('project.quotation', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#
#     @api.multi
#     def _get_total(self):
#         for record in self:
#             items_amount = 0
#             items_qty = 0
#             for item in record.items_used:
#                 items_amount += item.total
#                 items_qty += item.item_qty
#             record.items_total = items_amount
#             record.items_quantity = items_qty
#             if items_qty == 0:
#                 items_qty = 1
#             record.items_rate = round(items_amount / items_qty, 2)
#
#
# class MaterialUsedF(models.Model):
#     _name = 'material.usedf'
#     _description = 'Item Description'
#     _rec_name = 'item'
#
#     item = fields.Many2one('item.group', string='Item(s)', required=True, copy=True)
#     product_uom = fields.Many2one('quotation.uom', string='Unit(s)', required=True)
#     items_used = fields.One2many('material.used.item', 'detail_id', string='Items Used', copy=True)
#     items_quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
#     items_rate = fields.Float(compute='_get_total', string="Rate", copy=True)
#     items_total = fields.Float(compute='_get_total', string="Total", copy=True)
#     project_category = fields.Many2one(related='work_id.project_category', string="Project", required=True)
#     work_id = fields.Many2one('planned.workf', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#     #quote_id = fields.Many2one('project.quotation', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#
#     @api.multi
#     def _get_total(self):
#         for record in self:
#             items_amount = 0
#             items_qty = 0
#             for item in record.items_used:
#                 items_amount += item.total
#                 items_qty += item.item_qty
#             record.items_total = items_amount
#             record.items_quantity = items_qty
#             if items_qty == 0:
#                 items_qty = 1
#             record.items_rate = round(items_amount / items_qty, 2)
#
#
# class MaterialUsedG(models.Model):
#     _name = 'material.usedg'
#     _description = 'Item Description'
#     _rec_name = 'item'
#
#     item = fields.Many2one('item.group', string='Item(s)', required=True, copy=True)
#     product_uom = fields.Many2one('quotation.uom', string='Unit(s)', required=True)
#     items_used = fields.One2many('material.used.item', 'detail_id', string='Items Used', copy=True)
#     items_quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
#     items_rate = fields.Float(compute='_get_total', string="Rate", copy=True)
#     items_total = fields.Float(compute='_get_total', string="Total", copy=True)
#     project_category = fields.Many2one(related='work_id.project_category', string="Project", required=True)
#     work_id = fields.Many2one('planned.workg', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#     #quote_id = fields.Many2one('project.quotation', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#
#     @api.multi
#     def _get_total(self):
#         for record in self:
#             items_amount = 0
#             items_qty = 0
#             for item in record.items_used:
#                 items_amount += item.total
#                 items_qty += item.item_qty
#             record.items_total = items_amount
#             record.items_quantity = items_qty
#             if items_qty == 0:
#                 items_qty = 1
#             record.items_rate = round(items_amount / items_qty, 2)
#
#
# class MaterialUsedH(models.Model):
#     _name = 'material.usedh'
#     _description = 'Item Description'
#     _rec_name = 'item'
#
#     item = fields.Many2one('item.group', string='Item(s)', required=True, copy=True)
#     product_uom = fields.Many2one('quotation.uom', string='Unit(s)', required=True)
#     items_used = fields.One2many('material.used.item', 'detail_id', string='Items Used', copy=True)
#     items_quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
#     items_rate = fields.Float(compute='_get_total', string="Rate", copy=True)
#     items_total = fields.Float(compute='_get_total', string="Total", copy=True)
#     project_category = fields.Many2one(related='work_id.project_category', string="Project", required=True)
#     work_id = fields.Many2one('planned.workh', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#     #quote_id = fields.Many2one('project.quotation', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#
#     @api.multi
#     def _get_total(self):
#         for record in self:
#             items_amount = 0
#             items_qty = 0
#             for item in record.items_used:
#                 items_amount += item.total
#                 items_qty += item.item_qty
#             record.items_total = items_amount
#             record.items_quantity = items_qty
#             if items_qty == 0:
#                 items_qty = 1
#             record.items_rate = round(items_amount / items_qty, 2)
#
#
# class MaterialUsedI(models.Model):
#     _name = 'material.usedi'
#     _description = 'Item Description'
#     _rec_name = 'item'
#
#     item = fields.Many2one('item.group', string='Item(s)', required=True, copy=True)
#     product_uom = fields.Many2one('quotation.uom', string='Unit(s)', required=True)
#     items_used = fields.One2many('material.used.item', 'detail_id', string='Items Used', copy=True)
#     items_quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
#     items_rate = fields.Float(compute='_get_total', string="Rate", copy=True)
#     items_total = fields.Float(compute='_get_total', string="Total", copy=True)
#     project_category = fields.Many2one(related='work_id.project_category', string="Project", required=True)
#     work_id = fields.Many2one('planned.worki', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#     #quote_id = fields.Many2one('project.quotation', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#
#     @api.multi
#     def _get_total(self):
#         for record in self:
#             items_amount = 0
#             items_qty = 0
#             for item in record.items_used:
#                 items_amount += item.total
#                 items_qty += item.item_qty
#             record.items_total = items_amount
#             record.items_quantity = items_qty
#             if items_qty == 0:
#                 items_qty = 1
#             record.items_rate = round(items_amount / items_qty, 2)
#
#
# class MaterialUsedJ(models.Model):
#     _name = 'material.usedj'
#     _description = 'Item Description'
#     _rec_name = 'item'
#
#     item = fields.Many2one('item.group', string='Item(s)', required=True, copy=True)
#     product_uom = fields.Many2one('quotation.uom', string='Unit(s)', required=True)
#     items_used = fields.One2many('material.used.item', 'detail_id', string='Items Used', copy=True)
#     items_quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
#     items_rate = fields.Float(compute='_get_total', string="Rate", copy=True)
#     items_total = fields.Float(compute='_get_total', string="Total", copy=True)
#     project_category = fields.Many2one(related='work_id.project_category', string="Project", required=True)
#     work_id = fields.Many2one('planned.workj', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#     #quote_id = fields.Many2one('project.quotation', ondelete='cascade', domain="[('project_category', '=', project_category)]")
#
#     @api.multi
#     def _get_total(self):
#         for record in self:
#             items_amount = 0
#             items_qty = 0
#             for item in record.items_used:
#                 items_amount += item.total
#                 items_qty += item.item_qty
#             record.items_total = items_amount
#             record.items_quantity = items_qty
#             if items_qty == 0:
#                 items_qty = 1
#             record.items_rate = round(items_amount / items_qty, 2)

