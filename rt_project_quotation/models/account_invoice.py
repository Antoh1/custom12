
from odoo import models, fields, api


class ProjectQuoteInvoices(models.Model):
    _inherit = 'account.invoice'

    is_project_invoice = fields.Boolean(string="Is Project Invoice")
    project_quote = fields.Many2one('project.quotation', string="Project Quotation", help="Source Document")
    payment_details = fields.Text(compute='_get_defaults', string="Payment Details")
    payment_condition = fields.Text(compute='_get_defaults', string='Terms of Payment')

    @api.multi
    def action_invoice_paid(self):
        res = super(ProjectQuoteInvoices, self).action_invoice_paid()
        project_quot_obj = self.env['project.quotation'].search([('id', '=', self.project_quote.id)])
        for obj in project_quot_obj:
            obj.write({'state': 'invoiced'})
        return res

    @api.multi
    def _get_defaults(self):
        quote_defaults = self.env['quote.defaults'].search([('id', '=', 1)])
        self.payment_details = quote_defaults.payment_details
        self.payment_condition = quote_defaults.note
        
