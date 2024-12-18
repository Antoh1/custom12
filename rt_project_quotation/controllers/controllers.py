# -*- coding: utf-8 -*-
from odoo import http

# class RtProjectQuotation(http.Controller):
#     @http.route('/rt_project_quotation/rt_project_quotation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rt_project_quotation/rt_project_quotation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rt_project_quotation.listing', {
#             'root': '/rt_project_quotation/rt_project_quotation',
#             'objects': http.request.env['rt_project_quotation.rt_project_quotation'].search([]),
#         })

#     @http.route('/rt_project_quotation/rt_project_quotation/objects/<model("rt_project_quotation.rt_project_quotation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rt_project_quotation.object', {
#             'object': obj
#         })