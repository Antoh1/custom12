# -*- coding: utf-8 -*-
from odoo import http

# class RtVineto(http.Controller):
#     @http.route('/rt_vineto/rt_vineto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rt_vineto/rt_vineto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rt_vineto.listing', {
#             'root': '/rt_vineto/rt_vineto',
#             'objects': http.request.env['rt_vineto.rt_vineto'].search([]),
#         })

#     @http.route('/rt_vineto/rt_vineto/objects/<model("rt_vineto.rt_vineto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rt_vineto.object', {
#             'object': obj
#         })