odoo.define('pos_action_button.ActionButton', function(require){
"use strict"

 var pos_screens = require('point_of_sale.screens');
 var rpc = require('web.rpc');
 var gui = require('point_of_sale.gui');
 var popups = require('point_of_sale.popups');


 var DashButton = pos_screens.ActionButtonWidget.extend({
     template:'DashBtn',
     button_click : function(){
            var self = this;
            var selectedOrderline = this.pos.get_order().get_selected_orderline().product;
//            rpc.query({
//                model: 'product.product',
//                method: 'show_product_location',
//                args: [[], selectedOrderline.id]
//            }).then(function(result){
//                alert(selectedOrderline.display_name + '  Locations : \n' + result );
//            });
            var lst = showLocation();
            async function showLocation(){
                var loc_list = await rpc.query({
                model: 'product.product',
                method: 'show_product_location',
                args: [[], selectedOrderline.id]
                });
                self.gui.show_popup('selection',{
                title: selectedOrderline.display_name + " -- Location",
//                list: [
//                { label: loc_list,  item: 45 },
//                { label: 'bar foo', item: 'stuff' },
//                ],
                list: loc_list,
                confirm: function(item) {
                // get the item selected by the user.
                },
                cancel: function(){
               // user chose nothing
                }
            });
                return loc_list;
            };

        },
 });
  var SaleButton = pos_screens.ActionButtonWidget.extend({
     template:'SaleBtn',
     button_click : function(){
            var self = this;
            var selectedOrderline = this.pos.get_order().get_selected_orderline().product;
//            rpc.query({
//                model: 'product.product',
//                method: 'show_product_sales',
//                args: [[], selectedOrderline.id]
//            }).then(function(result){
//                alert(selectedOrderline.display_name + '   : \n' + result);
//            });
            var lst = showSales();
            async function showSales(){
                var sale_list = await rpc.query({
                model: 'product.product',
                method: 'show_product_sales',
                args: [[], selectedOrderline.id]
                });
                self.gui.show_popup('selection',{
                title: selectedOrderline.display_name + " -- Sale History",
//                list: [
//                { label: loc_list,  item: 45 },
//                { label: 'bar foo', item: 'stuff' },
//                ],
                list: sale_list,
                confirm: function(item) {
                // get the item selected by the user.
                },
                cancel: function(){
               // user chose nothing
                }
            });
                return sale_list;
            };

        },
 });
 //define the button
 pos_screens.define_action_button({
     'name':'dashboard',
     'widget':DashButton,
     'condition': function(){ return this.pos; },
 });
 pos_screens.define_action_button({
     'name':'salereport',
     'widget':SaleButton,
     'condition': function(){ return this.pos; },
 });
});