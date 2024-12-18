# -*- coding: utf-8 -*-
{
    'name': "rt_pharmacy",

    'summary': """
        This module is for managing all operations of a pharmacy
        from sales, inventory and prescription drugs""",

    'description': """
        Pharmacy management
    """,

    'author': "Ropetech Solutions",
    'website': "https://www.ropetech.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Pharmacy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_contract', 'hr', 'hr_payroll', 'stock', 'account', 'purchase', 'sale_management', 'point_of_sale', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/medicine_categories_data.xml',
        'data/medicine_company_data.xml',
        'data/medicine_data.xml',
        'views/views.xml',
        'wizard/medicine_expiry_report_wizard_view.xml',
        'views/medicine_type_view.xml',
        'views/appointment.xml',
        'views/medicine_category_view.xml',
        'views/medicine_company_view.xml',
        'views/pharmacy_sale_order_view.xml',
        'views/pharmacy_employee_view.xml',
        'views/pharmacy_medicine_view.xml',
        'views/pharmacy_purchase_order_view.xml',
        'views/customer_invoice_analysis_view.xml',
        'report/patient_report_template.xml',
        'report/pharmacy_report.xml',
        # 'views/',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}