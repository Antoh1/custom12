# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProjectQuotation(models.Model):
    _name = 'project.quotation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "work_date,name"

    @api.model
    def create(self, vals):  # generating sequence for ProjectQuotation model
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('project.quotation.code') or _('New')
        result = super(ProjectQuotation, self).create(vals)
        return result

    name = fields.Char(string='Quotation NO:', default=lambda self: _('New'))
    user_id = fields.Many2one('res.users', string='Attendant :', default=lambda self: self.env.user, tracking=True)
    work_date = fields.Datetime(string='Date')
    customer = fields.Many2one('res.partner', string='Client', domain="[('customer','=',True)]")
    # is_customer = fields.Boolean(related='customer.customer')
    details = fields.Text(string='Project Description', store=True, copy=True)
    size = fields.Char(string='Structure Size')
    # work = fields.Many2one('planned.work', string='Plannd Work') #domain="[('vehicle_ids', '=', client_id)]"
    # quantity = fields.Float(string='Quantity')
    # rate = fields.Float(string="Rate")
    #category = fields.Selection(related='work.category', string="Main Project")
    state = fields.Selection([
        ('waiting', 'Ready'),
        ('invoiced', 'Invoiced'),
        ('cancel', 'Quotation Canceled'),
    ], string='Status', readonly=True, default='waiting', track_visibility='onchange', select=True)
    state1 = fields.Selection([('draft', 'Draft'),
                               ('invoiced', 'Invoiced'),
                               ('completed', 'Completed')], default='draft', track_visibility='onchange')
    work_cost = fields.Float(compute='_get_total', string="Total Amount", copy=True)
    work_cost1 = fields.Float(compute='_get_total', string="Total", copy=True)
    work_cost2 = fields.Float(compute='_get_total', string="Total", copy=True)
    work_cost3 = fields.Float(compute='_get_total', string="Total", copy=True)
    work_cost4 = fields.Float(compute='_get_total', string="Total", copy=True)
    work_cost5 = fields.Float(compute='_get_total', string="Total", copy=True)
    work_cost6 = fields.Float(compute='_get_total', string="Total", copy=True)
    work_cost7 = fields.Float(compute='_get_total', string="Total", copy=True)
    work_cost8 = fields.Float(compute='_get_total', string="Total", copy=True)
    work_cost9 = fields.Float(compute='_get_total', string="Total", copy=True)
    work_cost10 = fields.Float(compute='_get_total', string="Total", copy=True)
    #project_category = fields.Many2one(related='work.project_cat', string="Project")
    project_category = fields.Many2one('quotation.project', string="Project", copy=True)
    project_category2 = fields.Many2one('quotation.project', string="Project", copy=True)
    project_category3 = fields.Many2one('quotation.project', string="Project", copy=True)
    project_category4 = fields.Many2one('quotation.project', string="Project", copy=True)
    project_category5 = fields.Many2one('quotation.project', string="Project", copy=True)
    project_category6 = fields.Many2one('quotation.project', string="Project", copy=True)
    project_category7 = fields.Many2one('quotation.project', string="Project", copy=True)
    project_category8 = fields.Many2one('quotation.project', string="Project", copy=True)
    project_category9 = fields.Many2one('quotation.project', string="Project", copy=True)
    project_category10 = fields.Many2one('quotation.project', string="Project", copy=True)
    planned_works = fields.One2many('planned.work', 'quote_id', string='Project A section(s)', copy=True)
    planned_works2 = fields.One2many('planned.workb', 'quote_id', string='Project B section(s)', copy=True)
    planned_works3 = fields.One2many('planned.workc', 'quote_id', string='Project C section(s)', copy=True)
    planned_works4 = fields.One2many('planned.workd', 'quote_id', string='Project D section(s)', copy=True)
    planned_works5 = fields.One2many('planned.worke', 'quote_id', string='Project E section(s)', copy=True)
    planned_works6 = fields.One2many('planned.workf', 'quote_id', string='Project F section(s)', copy=True)
    planned_works7 = fields.One2many('planned.workg', 'quote_id', string='Project G section(s)', copy=True)
    planned_works8 = fields.One2many('planned.workh', 'quote_id', string='Project H section(s)', copy=True)
    planned_works9 = fields.One2many('planned.worki', 'quote_id', string='Project I section(s)', copy=True)
    planned_works10 = fields.One2many('planned.workj', 'quote_id', string='Project J section(s)', copy=True)

    is_multi_project = fields.Boolean(string="Multi Project?", default=False)
    is_single_project = fields.Boolean(string="Single Project?", default=False)
    category = fields.Many2one(related='project_category', string="Main Project")
    # materials_used = fields.One2many('material.used', 'quote_id', string='Material Items', store=True, copy=True)
    invoice_count = fields.Integer(string="Invoice count", compute='_compute_invoice_count')
    date = fields.Datetime(string='Quote Date', default=fields.datetime.now(), select=True, copy=False)
    #note = fields.Text(related='quote_defaults.note', string='Note')

    # def _get_cat(self):
    #     for record in self:
    #         for work in record.planned_works:
    #             if work.category:
    #                 record.category = work.category
    #                 break
    @api.multi
    def _get_total(self):
        for record in self:
            quote_amount = 0
            works1 = 0
            works2 = 0
            works3 = 0
            works4 = 0
            works5 = 0
            works6 = 0
            works7 = 0
            works8 = 0
            works9 = 0
            works10 = 0
            for work in record.planned_works:
                quote_amount += work.total
                works1 += work.total
            for work in record.planned_works2:
                quote_amount += work.total
                works2 += work.total
            for work in record.planned_works3:
                works3 += work.total
                quote_amount += work.total
            for work in record.planned_works4:
                works4 += work.total
                quote_amount += work.total
            for work in record.planned_works5:
                works5 += work.total
                quote_amount += work.total
            for work in record.planned_works6:
                works6 += work.total
                quote_amount += work.total
            for work in record.planned_works7:
                works7 += work.total
                quote_amount += work.total
            for work in record.planned_works8:
                works8 += work.total
                quote_amount += work.total
            for work in record.planned_works9:
                works9 += work.total
                quote_amount += work.total
            for work in record.planned_works10:
                works10 += work.total
                quote_amount += work.total

            record.work_cost = quote_amount
            record.work_cost1 = works1
            record.work_cost2 = works2
            record.work_cost3 = works3
            record.work_cost4 = works4
            record.work_cost5 = works5
            record.work_cost6 = works6
            record.work_cost7 = works7
            record.work_cost8 = works8
            record.work_cost9 = works9
            record.work_cost10 = works10

    def cancel(self):
        self.state = 'cancel'

    def set_to_draft(self):
        self.state = 'waiting'

    def _get_defaults(self):
        return self.env['quote.defaults'].search([], limit=1)

    defaults = fields.Many2one('quote.defaults', string='Defaults', default=_get_defaults)
    #quote_defaults = fields.One2many('quote.defaults', 'quote_id', string='Quote Defaults')
    note = fields.Text(related='defaults.note', string='Note')
    pay_details = fields.Text(related='defaults.payment_details', string='Payment Details')

    @api.multi
    def _compute_invoice_count(self):
        for obj in self:
            #obj.request_count = self.env['lab.request'].search_count([('app_id', '=', obj.id)])
            obj.invoice_count = self.env['account.invoice'].search_count([('project_quote', '=', obj.id)])

    @api.multi
    def project_create_invoice(self):
        invoice_obj = self.env["account.invoice"]
        invoice_line_obj = self.env["account.invoice.line"]
        for quote in self:
            quote.write({'state': 'invoiced'})
            if quote.customer:
                curr_invoice = {
                    'partner_id': quote.customer.id,
                    'account_id': quote.customer.property_account_receivable_id.id,
                    'state': 'draft',
                    'type': 'out_invoice',
                    'date_invoice': str(datetime.now()),
                    'origin': "Quote # : " + quote.name,
                    'target': 'new',
                    'project_quote': quote.id,
                    'is_project_invoice': True,
                    'picking_count': 0
                }

                inv_ids = invoice_obj.create(curr_invoice)
                inv_id = inv_ids.id

                if inv_ids:
                    journal = self.env['account.journal'].search([('type', '=', 'sale')], limit=1)
                    prd_account_id = journal.default_credit_account_id.id
                    if quote.planned_works:
                        for line in quote.planned_works:
                            curr_invoice_line = {
                                'name': line.name.name,
                                'price_unit': line.rate or 0,
                                'quantity': line.quantity or 1.0,
                                'account_id': prd_account_id,
                                'invoice_id': inv_id,
                            }
                            invoice_line_obj.create(curr_invoice_line)

                    if quote.planned_works2:
                        for line in quote.planned_works2:
                            curr_invoice_line = {
                                'name': line.name.name,
                                'price_unit': line.rate or 0,
                                'quantity': line.quantity or 1.0,
                                'account_id': prd_account_id,
                                'invoice_id': inv_id,
                            }
                            invoice_line_obj.create(curr_invoice_line)

                    if quote.planned_works3:
                        for line in quote.planned_works3:
                            curr_invoice_line = {
                                'name': line.name.name,
                                'price_unit': line.rate or 0,
                                'quantity': line.quantity or 1.0,
                                'account_id': prd_account_id,
                                'invoice_id': inv_id,
                            }
                            invoice_line_obj.create(curr_invoice_line)

                    if quote.planned_works4:
                        for line in quote.planned_works4:
                            curr_invoice_line = {
                                'name': line.name.name,
                                'price_unit': line.rate or 0,
                                'quantity': line.quantity or 1.0,
                                'account_id': prd_account_id,
                                'invoice_id': inv_id,
                            }
                            invoice_line_obj.create(curr_invoice_line)

                # self.write({'state': 'invoiced'})
                view_id = self.env.ref('account.invoice_form').id
                return {
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'account.invoice',
                    'view_id': view_id,
                    'type': 'ir.actions.act_window',
                    'name': _('Project Quote Invoices'),
                    'res_id': inv_id
                }


class QuoteSettings(models.Model):
    _name = 'quote.defaults'
    _description = 'Quote Defaults'
    #_rec_name = 'note'

    name = fields.Char(string="Title", store=True, copy=True)
    note = fields.Text(string='Note', store=True, copy=True)
    payment_details = fields.Text(string='Payment Details', store=True, copy=True)
    #quote_id = fields.Many2one('project.quotation', ondelete='cascade')





