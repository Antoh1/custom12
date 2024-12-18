from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Medicines'

    is_medicine = fields.Boolean(string='Is Medicine?', default=True)
    is_prescription = fields.Boolean(string='Is Prescription Drug?')
    is_otc = fields.Boolean(string='Over The Counter Drug?', default=True)
    medicine_type_id = fields.Many2one('medicine.type', string='Medicine Type')
    category_id = fields.Many2one('product.category', string='Medicine Category')
    medicine_company_id = fields.Many2one('medicine.company', string='Medicine Company')
    expiry_date = fields.Date(string='Expiry Date')

    @api.onchange('is_prescription')
    def _prescription_change(self):
        for rec in self:
            if rec.is_prescription:
                rec.is_otc = False

    @api.onchange('is_otc')
    def _otc_change(self):
        for rec in self:
            if rec.is_otc:
                rec.is_prescription = False




class ProductProduct(models.Model):
    _inherit = 'product.product'
    _description = 'Medicines'

    # medicine_type_id = fields.Many2one('medicine.type', string='Medicine Type')
    # category_id = fields.Many2one('product.category', string='Medicine Category')
    # medicine_company_id = fields.Many2one('medicine.company', string='Medicine Company')
    # expiry_date = fields.Date(string='Expiry Date')
    medicine_type_id = fields.Many2one(related='product_tmpl_id.medicine_type_id', string='Medicine Type',
                                       store=True)
    category_id = fields.Many2one(related='product_tmpl_id.category_id', string='Medicine Category',
                                  store=True)
    medicine_company_id = fields.Many2one(related='product_tmpl_id.medicine_company_id',
                                          string='Medicine Company', store=True)
    expiry_date = fields.Date(related='product_tmpl_id.expiry_date', string='Expiry Date', store=True)
