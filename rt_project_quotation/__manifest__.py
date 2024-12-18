# -*- coding: utf-8 -*-
{
    'name': "rt_project_quotation",

    'summary': """
        Module for project specific sale workflow, from quotation to payment""",

    'description': """
        Module for project specific sale workflow, from quotation to payment
    """,

    'author': "Ropetech Solutions",
    'website': "https://www.ropetech.co.ke",
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale', 'account', 'sale_management', 'point_of_sale','report_xlsx'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/quotation_data.xml',
        'data/project_section_data.xml',
        'data/material_used_group_data.xml',
        'views/rt_project.xml',
        'views/item_category_view.xml',
        'views/quotation_project.xml',
        'views/material_used.xml',
        'views/project_works.xml',
        'views/product_view.xml',
        'views/config_setting.xml',
        'views/sale_order.xml',
        'views/stock_picking.xml',
        'views/account_invoice.xml',
        'views/templates.xml',
        'views/assets.xml',
        'views/quote_report_template.xml',
        'report/delivery_note.xml',
        'report/payment_receipt.xml',
        'views/report_invoice.xml',
        'views/material_checklist.xml',
        'views/project_report.xml',
    ],
    'qweb': ["static/src/xml/pos.xml"],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}