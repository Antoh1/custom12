# -*- coding: utf-8 -*-
{
    'name': "rt_m2measure",

    'summary': """
        Module to allow addition of Length and width for products
        measured in Square Meters""",

    'description': """
        Square Meters Module
    """,

    'author': "Ropetech Solutions",
    'website': "https://www.ropetech.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'rt_project_quotation'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/import.xml',
        'views/pos_config.xml',
        'views/product_view.xml',
        'views/pos_order_line.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}