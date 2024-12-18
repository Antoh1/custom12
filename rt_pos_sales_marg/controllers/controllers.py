# -*- coding: utf-8 -*-
from odoo import http

# class RtPosSalesMarg(http.Controller):
#     @http.route('/rt_pos_sales_marg/rt_pos_sales_marg/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rt_pos_sales_marg/rt_pos_sales_marg/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rt_pos_sales_marg.listing', {
#             'root': '/rt_pos_sales_marg/rt_pos_sales_marg',
#             'objects': http.request.env['rt_pos_sales_marg.rt_pos_sales_marg'].search([]),
#         })

#     @http.route('/rt_pos_sales_marg/rt_pos_sales_marg/objects/<model("rt_pos_sales_marg.rt_pos_sales_marg"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rt_pos_sales_marg.object', {
#             'object': obj
#         })