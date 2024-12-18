"use strict";

odoo.define('pos_extended_interface.popups', function (require) {

    var core = require('web.core');
    var _t = core._t;
    var gui = require('point_of_sale.gui');
    var PopupWidget = require('point_of_sale.popups');   
    var qweb = core.qweb;
    
    var popup_orderline_measure = PopupWidget.extend({
        template: 'popup_orderline_measure',
        show: function (options) {
            var self = this;
            options = options || {};

            this._super(options);
            this.renderElement();

            $('.confirm').click(function () {
                self.click_confirm();
            });
            $('.cancel').click(function () {
                self.gui.close_popup();
            });
        },
        click_confirm: function () {

            var length = this.$('#length').val();
            var width = this.$('#width').val();
            var quantity_sqm = this.$('#quantity_sqm').val();
            var sqm_total = length*width*quantity_sqm
            var product_measures = {'length':this.$('#length').val(),
                                 'width':this.$('#width').val(),
                                 'quantity_sqm':this.$('#quantity_sqm').val(),
                                 'total_sqm':sqm_total,
                                 }
            this.gui.close_popup();
            if (this.options.confirm) {
                this.options.confirm.call(this, product_measures);
            }
        }
    });
    gui.define_popup({name: 'popup_orderline_measure', widget: popup_orderline_measure});

    

});
