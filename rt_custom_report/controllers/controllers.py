# -*- coding: utf-8 -*-
from odoo import http

# class RtCustomReport(http.Controller):
#     @http.route('/rt_custom_report/rt_custom_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rt_custom_report/rt_custom_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rt_custom_report.listing', {
#             'root': '/rt_custom_report/rt_custom_report',
#             'objects': http.request.env['rt_custom_report.rt_custom_report'].search([]),
#         })

#     @http.route('/rt_custom_report/rt_custom_report/objects/<model("rt_custom_report.rt_custom_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rt_custom_report.object', {
#             'object': obj
#         })