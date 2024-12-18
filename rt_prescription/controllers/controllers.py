# -*- coding: utf-8 -*-
from odoo import http

# class RtPrescription(http.Controller):
#     @http.route('/rt_prescription/rt_prescription/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rt_prescription/rt_prescription/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rt_prescription.listing', {
#             'root': '/rt_prescription/rt_prescription',
#             'objects': http.request.env['rt_prescription.rt_prescription'].search([]),
#         })

#     @http.route('/rt_prescription/rt_prescription/objects/<model("rt_prescription.rt_prescription"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rt_prescription.object', {
#             'object': obj
#         })