# -*- coding: utf-8 -*-
{
    'name': "ProductFields",

    'summary': """
        This module adds more fields to the product display view""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Tirop",
    'website': "http://www.ropetech.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'point_of_sale','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}