"use strict";

odoo.define('pos_extended_interface.order', function (require) {

    var utils = require('web.utils');
    var round_pr = utils.round_precision;
    var models = require('point_of_sale.models');
    var core = require('web.core');
    var qweb = core.qweb;
    var _t = core._t;

    models.load_fields('product.product', ['sqm_measures','is_m2']);
    var _super_Order = models.Order.prototype;

    models.Order = models.Order.extend({
        initialize: function (attributes, options) {
            _super_Order.initialize.apply(this, arguments);
            var self = this;
            if (!this.note) {
                this.note = '';
            }
        },
        init_from_JSON: function (json) {
            var res = _super_Order.init_from_JSON.apply(this, arguments);
            if (json.note) {
                this.note = json.note
            }
            return res;
        },
        export_as_JSON: function () {
            var json = _super_Order.export_as_JSON.apply(this, arguments);
            if (this.note) {
                json.note = this.note;
            }
            return json;
        },
        export_for_printing: function () {
            var receipt = _super_Order.export_for_printing.call(this);
            receipt['note'] = this.note;
            receipt['signature'] = this.signature;
            return receipt;
        },
        add_product: function (product, options) {
            var res = _super_Order.add_product.apply(this, arguments);
            var line = this.get_selected_orderline();

            if(line.get_product().is_m2){
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
            }
            return res;
        },
        set_note: function (note) {
            this.note = note;
            this.trigger('change', this);
        },
        get_note: function (note) {
            return this.note;
        },
    });

    var _super_Orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        initialize: function (attributes, options) {
            var res = _super_Orderline.initialize.apply(this, arguments);
            this.note = this.note || "";
            this.length = this.length;
            this.width = this.width;
            this.quantity_sqm = this.quantity_sqm;
            return res;
        },
        init_from_JSON: function (json) {
            var res = _super_Orderline.init_from_JSON.apply(this, arguments);
            if (json.length) {
               this.length = this.set_line_length(json.length);
            };
            if (json.width) {
               this.width = this.set_line_width(json.width);
            };
            if (json.quantity_sqm) {
               this.quantity_sqm = this.set_line_quantity_sqm(json.quantity_sqm);
            };
        },
        export_as_JSON: function () {
            var json = _super_Orderline.export_as_JSON.apply(this, arguments);
            if (this.length) {
                json.length = this.get_line_length();
            };
            if (this.width) {
                json.width = this.get_line_width();
            };
            if (this.quantity_sqm) {
                json.quantity_sqm = this.get_line_quantity_sqm();
            };
            return json;
        },
        clone: function () {
            var orderline = _super_Orderline.clone.call(this);
            orderline.length = this.length;
            orderline.width = this.width;
            orderline.quantity_sqm = this.quantity_sqm;
            return orderline;
        },
        export_for_printing: function () {
            var receipt_line = _super_Orderline.export_for_printing.apply(this, arguments);
            receipt_line['length'] = this.length || '';
            receipt_line['width'] = this.width || '';
            receipt_line['quantity_sqm'] = this.quantity_sqm || '';
            return receipt_line;
        },
        set_line_length: function (length) {
            this.length = length;
            this.trigger('change', this);
        },
        get_line_length: function () {
            return this.length;
        },
        set_line_width: function (width) {
            this.width = width;
            this.trigger('change', this);
        },
        get_line_width: function () {
            return this.width;
        },
        set_line_quantity_sqm: function (quantity_sqm) {
            this.quantity_sqm = quantity_sqm;
            this.trigger('change', this);
        },
        get_line_quantity_sqm: function () {
            return this.quantity_sqm;
        },
    });    
    
});
