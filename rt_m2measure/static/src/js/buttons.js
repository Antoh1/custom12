"use strict";

odoo.define('rt_prescription.buttons', function (require) {
    var screens = require('point_of_sale.screens');
    var core = require('web.core');
    var WebClient = require('web.AbstractWebClient');
    var models = require('point_of_sale.models');
    
    var _t = core._t;    
    var qweb = core.qweb;

    
    var button_orderline_measure = screens.ActionButtonWidget.extend({
        template: 'button_orderline_measure',
        button_click: function () {
            var line = this.pos.get_order().get_selected_orderline();
            if (line && line.get_product().is_m2) {
                this.pos.gui.show_popup('popup_orderline_measure', {
                    title: _t(line.get_product().display_name + ' Measurements'),
                    length: line.get_line_length(),
                    width: line.get_line_width(),
                    quantity_sqm: line.get_line_quantity_sqm(),
                    confirm: function (product_measures) {
                        line.set_line_length(product_measures['length']);
                        line.set_line_width(product_measures['width']);
                        line.set_line_quantity_sqm(product_measures['quantity_sqm']);
                        line.set_quantity(product_measures['total_sqm']);
                    }
                });
            } else {
                this.pos.gui.show_popup('confirm', {
                    title: 'Hey!!! Really!!',
                    body: 'Please select Product Measured in SQM'
                })
            }
        }
    });    
    
    screens.define_action_button({
        'name': 'button_orderline_measure',
        'widget': button_orderline_measure,
        'condition': function () {
            return this.pos.config.orderline_note;
        }
    });
    
 
});    
