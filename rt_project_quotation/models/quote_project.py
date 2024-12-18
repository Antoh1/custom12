# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProjectMain(models.Model):
    _name = 'quotation.project'
    _description = 'Project'
    #_rec_name = 'note'

    name = fields.Char(string="Project", store=True, required=True, copy=True)
    project_detail = fields.Text(string='Project Details', store=True, copy=True)


class ProjectSection(models.Model):
    _name = 'quotation.project.section'
    _description = 'Project Section'

    name = fields.Char(string="Project Section", store=True, required=True, copy=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)
    # project_category2 = fields.Many2one('quotation.project', string="Project"))


class LocalUOM(models.Model):
    _name = 'quotation.uom'
    _description = 'Quotation group Items Unit of Measure'

    name = fields.Char(string="Unit")


class ItemGroup(models.Model):
    _name = 'item.group'
    _description = 'Item used Grouping'

    name = fields.Char(string="Item(s)", required=True, copy=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)


class ItemUsed(models.Model):
    _name = 'material.used.item'
    _rec_name = 'item'
    _description = 'Items Used'

    item = fields.Many2one('product.product', string='Products')
    item_category = fields.Many2one(related='item.categ_id', string='Item Category')
    item_qty = fields.Integer(string='Quantity', copy=True)
    product_uom = fields.Char(string='Units')
    price = fields.Float(string='Unit Price', copy=True)
    total = fields.Float(string='Total Price')
    # project_category = fields.Many2one('quotation.project', string="Project")
    project_category = fields.Many2one(related='detail_id.project_category', string="Project")
    detail_id = fields.Many2one('material.used', ondelete='cascade', domain="[('project_category', '=', project_category)]")

    @api.onchange('item')
    def get_price(self):
        self.price = self.item.lst_price
        self.product_uom = self.item.uom_name

    @api.onchange('item_qty')
    def get_total(self):
        self.total = self.price * self.item_qty

