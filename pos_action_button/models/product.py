# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def show_product_location(self, product):
        sq = self.env['stock.quant'].search([('location_id.usage', '=', 'internal'), ('product_id', '=', product)])
        prod_locations = []
        for q in sq:
            prod_locations.append({'label': str(q.location_id.complete_name.split("Locations/")[1]) + " --------- " + str(q.quantity) + " Unit(s)", 'item': q.quantity})
        res = ""
        # for dt in prod_locations:
        #     res += str(dt['name'])+":   "+str(dt['quantity']) + " Unit(s)" + "\n"
        return prod_locations

    def show_product_sales(self, product):
        product_sale = self.env['sale.report'].search([('partner_id','!=',False),('product_id', '=', product)])
        prod_sales = []
        for s in product_sale:
            prod_sales.append({'Date':s.date,'Customer':s.partner_id.name,'Quantity':s.qty_delivered,'Price':s.price_total})
        res = ""
        sale_list = []
        for ps in prod_sales:
            #res += str(ps['Customer'])+" --- "+str(ps['Date']).split(" ")[0]+" --- "+str(ps['Quantity'])+" --- "+str(ps['Price']/ps['Quantity']) + "\n"
            sale_list.append({'label': str(ps['Customer'])+" ----- "+str(ps['Date']).split(" ")[0]+" ----- "+str(ps['Quantity'])+" Unit(s)"+" ----- "+str(ps['Price']/ps['Quantity']), 'item': ps['Quantity']})
        return sale_list
