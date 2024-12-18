# -*- coding: utf-8 -*-
from odoo import http

# class RtM2measure(http.Controller):
#     @http.route('/rt_m2measure/rt_m2measure/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rt_m2measure/rt_m2measure/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rt_m2measure.listing', {
#             'root': '/rt_m2measure/rt_m2measure',
#             'objects': http.request.env['rt_m2measure.rt_m2measure'].search([]),
#         })

#     @http.route('/rt_m2measure/rt_m2measure/objects/<model("rt_m2measure.rt_m2measure"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rt_m2measure.object', {
#             'object': obj
#         })