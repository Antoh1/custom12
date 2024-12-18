# -*- coding: utf-8 -*-
# from odoo import http


# class RtPosAnalysis(http.Controller):
#     @http.route('/rt_pos_analysis/rt_pos_analysis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rt_pos_analysis/rt_pos_analysis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rt_pos_analysis.listing', {
#             'root': '/rt_pos_analysis/rt_pos_analysis',
#             'objects': http.request.env['rt_pos_analysis.rt_pos_analysis'].search([]),
#         })

#     @http.route('/rt_pos_analysis/rt_pos_analysis/objects/<model("rt_pos_analysis.rt_pos_analysis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rt_pos_analysis.object', {
#             'object': obj
#         })
