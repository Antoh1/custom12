# -*- coding: utf-8 -*-
# Copyright 2020 Dishon Kadoh <https://realestdon.github.io/>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Kenyan Chart of Accounts',
    'version': '12.0.0.1',
    'category': 'Localization',
    'license': 'AGPL-3',
    'description': """
        Basic Kenyan Chart of Accounts localisation for Odoo:
        =====================================================
        * A generic chart of accounts
        * Defines templates for sale and purchase VAT
        * Defines tax templates
   """,
    'author': 'Dishon Kadoh',
    'website': 'https://realestdon.github.io/',
    'images': ['static/description/banner.png'],
    'depends': ['account', 'base_vat'],
    'data': [
        'data/account.account.tag.csv',
        'data/account.tax.group.csv',
        'data/account_chart_template_data.xml',
        'data/account.account.template.csv',
        'data/account_tax_template_data.xml',
        'data/account_chart_template_post_data.xml',
        'data/account_chart_template_configure_data.xml',
    ],
}
