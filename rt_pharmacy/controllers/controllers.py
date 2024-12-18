# -*- coding: utf-8 -*-
from odoo import http

# class RtPharmacy(http.Controller):
#     @http.route('/rt_pharmacy/rt_pharmacy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rt_pharmacy/rt_pharmacy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rt_pharmacy.listing', {
#             'root': '/rt_pharmacy/rt_pharmacy',
#             'objects': http.request.env['rt_pharmacy.rt_pharmacy'].search([]),
#         })

#     @http.route('/rt_pharmacy/rt_pharmacy/objects/<model("rt_pharmacy.rt_pharmacy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rt_pharmacy.object', {
#             'object': obj
#         })