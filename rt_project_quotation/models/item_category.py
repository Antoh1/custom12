from datetime import date, datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProjectProduct(models.Model):
    _inherit = 'product.template'

    item_category = fields.Many2one()
    pro_category = fields.Selection([
                                    ('green', 'GreenHouse'),
                                    ('solar', 'Solar Dryer'),
                                    ('drill', 'Borehole Drilling'),
                                    ('irrigation', 'irrigation System'),
                                    ], required=True, default='green', string="Project Category")


class ProjectProductP(models.Model):
    _inherit = 'product.product'

    # pro_category = fields.Selection([
    #                                 ('green', 'GreenHouse'),
    #                                 ('solar', 'Solar Dryer'),
    #                                 ('drill', 'Borehole Drilling'),
    #                                 ('irrigation', 'irrigation System'),
    #                                 ], required=True, default='green', string="Project Category")


class ItemCategory(models.Model):
    _inherit = 'product.category'
    _description = 'Item Category'

    # custom fields specific to medicine category
    is_project_item = fields.Boolean(string='Is Project Category?')
    project_category = fields.Many2one('quotation.project', string="Project")
