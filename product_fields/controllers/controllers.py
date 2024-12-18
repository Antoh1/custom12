# -*- coding: utf-8 -*-
from odoo import http

# class C:\users\user\desktop\modules\productFields(http.Controller):
#     @http.route('/c:\users\user\desktop\modules\product_fields/c:\users\user\desktop\modules\product_fields/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:\users\user\desktop\modules\product_fields/c:\users\user\desktop\modules\product_fields/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:\users\user\desktop\modules\product_fields.listing', {
#             'root': '/c:\users\user\desktop\modules\product_fields/c:\users\user\desktop\modules\product_fields',
#             'objects': http.request.env['c:\users\user\desktop\modules\product_fields.c:\users\user\desktop\modules\product_fields'].search([]),
#         })

#     @http.route('/c:\users\user\desktop\modules\product_fields/c:\users\user\desktop\modules\product_fields/objects/<model("c:\users\user\desktop\modules\product_fields.c:\users\user\desktop\modules\product_fields"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:\users\user\desktop\modules\product_fields.object', {
#             'object': obj
#         })