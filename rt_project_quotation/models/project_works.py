# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError
# from odoo.tools.float_utils import float_split_str
from odoo.tools.float_utils import float_round


class PlannedWork(models.Model):
    _name = 'planned.work'
    name = fields.Many2one('quotation.project.section', string='Project Section', required=True)
    labour_rate = fields.Float(string="Labour Rate(%)", required=True, copy=True, store=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)
    materials_used = fields.One2many('material.used', 'work_id', string='Materials Used', copy=True)
    quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
    rate = fields.Float(compute='_get_total', string="Rate", copy=True)
    total = fields.Float(compute='_get_total', string="Total", copy=True)
    quote_id = fields.Many2one('project.quotation', ondelete='cascade', copy=True)

    @api.multi
    def _get_total(self):
        for record in self:
            work_amount = 0
            work_qty = 0
            for item in record.materials_used:
                work_amount += item.items_total
                work_qty += item.items_quantity
            record.total = round(float_round(work_amount * ((record.labour_rate / 100) + 1), precision_rounding=0.01),2)
            record.quantity = work_qty
            if work_qty == 0:
                work_qty = 1
            record.rate = round(float_round(record.total / work_qty, precision_rounding=0.01),2)


class PlannedWorkB(models.Model):
    _name = 'planned.workb'
    name = fields.Many2one('quotation.project.section', string='Project Section', required=True)
    labour_rate = fields.Float(string="Labour Rate(%)", required=True, copy=True, store=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)
    # project_catb = fields.Many2one(related='quote_id.project_category', string="Project B")
    materials_used = fields.One2many('material.used', 'work_idb', string='Materials Used', copy=True)
    quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
    rate = fields.Float(compute='_get_total', string="Rate", copy=True)
    total = fields.Float(compute='_get_total', string="Total", copy=True)
    quote_id = fields.Many2one('project.quotation', ondelete='cascade', copy=True)

    # @api.onchange('quote_id')
    @api.multi
    def _get_total(self):
        for record in self:
            work_amount = 0
            work_qty = 0
            for item in record.materials_used:
                work_amount += item.items_total
                work_qty += item.items_quantity
            record.total = round(float_round(work_amount * ((record.labour_rate / 100) + 1), precision_rounding=0.01),2)
            record.quantity = work_qty
            if work_qty == 0:
                work_qty = 1
            record.rate = round(float_round(record.total / work_qty, precision_rounding=0.01),2)


class PlannedWorkC(models.Model):
    _name = 'planned.workc'
    name = fields.Many2one('quotation.project.section', string='Project Section', required=True)
    labour_rate = fields.Float(string="Labour Rate(%)", required=True, copy=True, store=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)
    project_catc = fields.Many2one(related='quote_id.project_category', string="Project C")
    materials_used = fields.One2many('material.used', 'work_idc', string='Materials Used', copy=True)
    quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
    rate = fields.Float(compute='_get_total', string="Rate", copy=True)
    total = fields.Float(compute='_get_total', string="Total", copy=True)
    quote_id = fields.Many2one('project.quotation', ondelete='cascade', copy=True)

    # @api.onchange('quote_id')
    @api.multi
    def _get_total(self):
        for record in self:
            work_amount = 0
            work_qty = 0
            for item in record.materials_used:
                work_amount += item.items_total
                work_qty += item.items_quantity
            record.total = round(float_round(work_amount * ((record.labour_rate / 100) + 1), precision_rounding=0.01),2)
            record.quantity = work_qty
            if work_qty == 0:
                work_qty = 1
            record.rate = round(float_round(record.total / work_qty, precision_rounding=0.01),2)


class PlannedWorkD(models.Model):
    _name = 'planned.workd'
    name = fields.Many2one('quotation.project.section', string='Project Section', required=True)
    labour_rate = fields.Float(string="Labour Rate(%)", required=True, copy=True, store=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)
    materials_used = fields.One2many('material.used', 'work_idd', string='Materials Used', copy=True)
    quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
    rate = fields.Float(compute='_get_total', string="Rate", copy=True)
    total = fields.Float(compute='_get_total', string="Total", copy=True)
    quote_id = fields.Many2one('project.quotation', ondelete='cascade', store=True, copy=True)

    # @api.onchange('quote_id')
    @api.multi
    def _get_total(self):
        for record in self:
            work_amount = 0
            work_qty = 0
            for item in record.materials_used:
                work_amount += item.items_total
                work_qty += item.items_quantity
            record.total = round(float_round(work_amount * ((record.labour_rate / 100) + 1), precision_rounding=0.01),2)
            record.quantity = work_qty
            if work_qty == 0:
                work_qty = 1
            record.rate = round(float_round(record.total / work_qty, precision_rounding=0.01),2)


class PlannedWorkE(models.Model):
    _name = 'planned.worke'
    name = fields.Many2one('quotation.project.section', string='Project Section', required=True)
    labour_rate = fields.Float(string="Labour Rate(%)", required=True, copy=True, store=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)
    materials_used = fields.One2many('material.used', 'work_ide', string='Materials Used', copy=True)
    quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
    rate = fields.Float(compute='_get_total', string="Rate", copy=True)
    total = fields.Float(compute='_get_total', string="Total", copy=True)
    quote_id = fields.Many2one('project.quotation', ondelete='cascade', store=True, copy=True)

    # @api.onchange('quote_id')
    @api.multi
    def _get_total(self):
        for record in self:
            work_amount = 0
            work_qty = 0
            for item in record.materials_used:
                work_amount += item.items_total
                work_qty += item.items_quantity
            record.total = round(float_round(work_amount * ((record.labour_rate / 100) + 1), precision_rounding=0.01),2)
            record.quantity = work_qty
            if work_qty == 0:
                work_qty = 1
            record.rate = round(float_round(record.total / work_qty, precision_rounding=0.01),2)


class PlannedWorkF(models.Model):
    _name = 'planned.workf'
    name = fields.Many2one('quotation.project.section', string='Project Section', required=True)
    labour_rate = fields.Float(string="Labour Rate(%)", required=True, copy=True, store=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)
    materials_used = fields.One2many('material.used', 'work_idf', string='Materials Used', copy=True)
    quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
    rate = fields.Float(compute='_get_total', string="Rate", copy=True)
    total = fields.Float(compute='_get_total', string="Total", copy=True)
    quote_id = fields.Many2one('project.quotation', ondelete='cascade', store=True, copy=True)

    # @api.onchange('quote_id')
    @api.multi
    def _get_total(self):
        for record in self:
            work_amount = 0
            work_qty = 0
            for item in record.materials_used:
                work_amount += item.items_total
                work_qty += item.items_quantity
            record.total = round(float_round(work_amount * ((record.labour_rate / 100) + 1), precision_rounding=0.01),2)
            record.quantity = work_qty
            if work_qty == 0:
                work_qty = 1
            record.rate = round(float_round(record.total / work_qty, precision_rounding=0.01),2)


class PlannedWorkG(models.Model):
    _name = 'planned.workg'
    name = fields.Many2one('quotation.project.section', string='Project Section', required=True)
    labour_rate = fields.Float(string="Labour Rate(%)", required=True, copy=True, store=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)
    materials_used = fields.One2many('material.used', 'work_idg', string='Materials Used', copy=True)
    quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
    rate = fields.Float(compute='_get_total', string="Rate", copy=True)
    total = fields.Float(compute='_get_total', string="Total", copy=True)
    quote_id = fields.Many2one('project.quotation', ondelete='cascade', store=True, copy=True)

    # @api.onchange('quote_id')
    @api.multi
    def _get_total(self):
        for record in self:
            work_amount = 0
            work_qty = 0
            for item in record.materials_used:
                work_amount += item.items_total
                work_qty += item.items_quantity
            record.total = round(float_round(work_amount * ((record.labour_rate / 100) + 1), precision_rounding=0.01),2)
            record.quantity = work_qty
            if work_qty == 0:
                work_qty = 1
            record.rate = round(float_round(record.total / work_qty, precision_rounding=0.01),2)


class PlannedWorkH(models.Model):
    _name = 'planned.workh'
    name = fields.Many2one('quotation.project.section', string='Project Section', required=True)
    labour_rate = fields.Float(string="Labour Rate(%)", required=True, copy=True, store=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)
    materials_used = fields.One2many('material.used', 'work_idh', string='Materials Used', copy=True)
    quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
    rate = fields.Float(compute='_get_total', string="Rate", copy=True)
    total = fields.Float(compute='_get_total', string="Total", copy=True)
    quote_id = fields.Many2one('project.quotation', ondelete='cascade', store=True, copy=True)

    # @api.onchange('quote_id')
    @api.multi
    def _get_total(self):
        for record in self:
            work_amount = 0
            work_qty = 0
            for item in record.materials_used:
                work_amount += item.items_total
                work_qty += item.items_quantity
            record.total = round(float_round(work_amount * ((record.labour_rate / 100) + 1), precision_rounding=0.01),2)
            record.quantity = work_qty
            if work_qty == 0:
                work_qty = 1
            record.rate = round(float_round(record.total / work_qty, precision_rounding=0.01),2)


class PlannedWorkI(models.Model):
    _name = 'planned.worki'
    name = fields.Many2one('quotation.project.section', string='Project Section', required=True)
    labour_rate = fields.Float(string="Labour Rate(%)", required=True, copy=True, store=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)
    materials_used = fields.One2many('material.used', 'work_idi', string='Materials Used', copy=True)
    quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
    rate = fields.Float(compute='_get_total', string="Rate", copy=True)
    total = fields.Float(compute='_get_total', string="Total", copy=True)
    quote_id = fields.Many2one('project.quotation', ondelete='cascade', store=True, copy=True)

    # @api.onchange('quote_id')
    @api.multi
    def _get_total(self):
        for record in self:
            work_amount = 0
            work_qty = 0
            for item in record.materials_used:
                work_amount += item.items_total
                work_qty += item.items_quantity
            record.total = round(float_round(work_amount * ((record.labour_rate / 100) + 1), precision_rounding=0.01),2)
            record.quantity = work_qty
            if work_qty == 0:
                work_qty = 1
            record.rate = round(float_round(record.total / work_qty, precision_rounding=0.01),2)


class PlannedWorkJ(models.Model):
    _name = 'planned.workj'
    name = fields.Many2one('quotation.project.section', string='Project Section', required=True)
    labour_rate = fields.Float(string="Labour Rate(%)", required=True, copy=True, store=True)
    project_category = fields.Many2one('quotation.project', string="Project", required=True)
    materials_used = fields.One2many('material.used', 'work_idj', string='Materials Used', copy=True)
    quantity = fields.Integer(compute='_get_total', string="Quantity", copy=True)
    rate = fields.Float(compute='_get_total', string="Rate", copy=True)
    total = fields.Float(compute='_get_total', string="Total", copy=True)
    quote_id = fields.Many2one('project.quotation', ondelete='cascade', store=True, copy=True)

    # @api.onchange('quote_id')
    @api.multi
    def _get_total(self):
        for record in self:
            work_amount = 0
            work_qty = 0
            for item in record.materials_used:
                work_amount += item.items_total
                work_qty += item.items_quantity
            record.total = round(float_round(work_amount * ((record.labour_rate / 100) + 1), precision_rounding=0.01),2)
            record.quantity = work_qty
            if work_qty == 0:
                work_qty = 1
            record.rate = round(float_round(record.total / work_qty, precision_rounding=0.01),2)

