# -*- coding: utf-8 -*-
{
    'name': "rt_vineto",

    'summary': """
        Module to modify report documents - Sale Order, Quotation, Invoice""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ropetech Solutions",
    'website': "https://www.ropetech.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/document_defaults.xml',
        'views/sale_order.xml',
        'views/stock_picking.xml',
        'views/account_invoice.xml',
        'report/invoice_report_dot.xml',
        'report/delivery_note.xml',
        'report/quotation_report_template.xml',
        'report/sale_report_templates.xml',
        'report/report_invoice.xml',
        # 'report/custom_header.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}