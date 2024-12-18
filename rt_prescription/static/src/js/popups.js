"use strict";

odoo.define('pos_extended_interface.popups', function (require) {

    var core = require('web.core');
    var _t = core._t;
    var gui = require('point_of_sale.gui');
    var PopupWidget = require('point_of_sale.popups');   
    var qweb = core.qweb;
    
    var popup_orderline_note = PopupWidget.extend({
        template: 'popup_orderline_note',
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
            
//            var value = this.$('input,textarea').val();
            var value = this.$('#hospital').val();
            var patient = this.$('#patient').val();
            var patient_no = this.$('#patient_no').val();
            var doctor = this.$('#doctor').val();
            var doctor_no = this.$('#doctor_no').val();
            var hospital = this.$('#hospital').val();
            var prescription = this.$('#prescription').val();
            var patient_presc = {'patient':this.$('#patient').val(),
                                 'patient_no':this.$('#patient_no').val(),
                                 'hospital':this.$('#hospital').val(),
                                 'doctor':this.$('#doctor').val(),
                                 'doctor_no':this.$('#doctor_no').val(),
                                 'prescription':this.$('#prescription').val()}
            this.gui.close_popup();
            if (this.options.confirm) {
                this.options.confirm.call(this, patient_presc);
            }
        }
    });
    gui.define_popup({name: 'popup_orderline_note', widget: popup_orderline_note});

    var popup_order_note = PopupWidget.extend({
        template: 'popup_order_note',
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
            
            var value = this.$('input,textarea').val();
            this.gui.close_popup();
            if (this.options.confirm) {
                this.options.confirm.call(this, value);
            }
        }
    });
    gui.define_popup({name: 'popup_order_note', widget: popup_order_note});   
    

});
