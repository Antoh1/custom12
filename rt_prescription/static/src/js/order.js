"use strict";

odoo.define('pos_extended_interface.order', function (require) {

    var utils = require('web.utils');
    var round_pr = utils.round_precision;
    var models = require('point_of_sale.models');
    var core = require('web.core');
    var qweb = core.qweb;
    var _t = core._t;

    models.load_fields('product.product', ['medicine_type_id','category_id','medicine_company_id','expiry_date','is_otc','is_prescription']);
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
            console.log(this.get_selected_orderline())
            var line = this.get_selected_orderline();
            if(line.get_product().expiry_date){
                var current_date = new Date();
                var xd = new Date(line.get_product().expiry_date);
                var expiry = (xd - current_date)/86400000;
                if(expiry<=4){
                    this.pos.gui.show_popup('alert', {
                                title: _t(line.get_product().display_name + ' Expiry'),
                                body: _.str.sprintf(
                                  _t(line.get_product().display_name + ' expires in ' + Math.round(expiry) + ' days'),
                                ),
                            });
                };
            };

            if(line.get_product().is_prescription){
                this.pos.gui.show_popup('popup_orderline_note', {
                    title: _t(line.get_product().display_name + ' Prescription'),
                    value: line.get_line_note(),
                    patient: line.get_line_patient(),
                    patient_no: line.get_line_patient_no(),
                    hospital: line.get_line_hospital(),
                    doctor: line.get_line_doctor(),
                    doctor_no: line.get_line_doctor_no(),
                    prescription: line.get_line_prescription(),
                    confirm: function (patient_presc) {
//                        line.set_line_note(note);
                        line.set_line_patient(patient_presc['patient']);
                        line.set_line_patient_no(patient_presc['patient_no']);
                        line.set_line_hospital(patient_presc['hospital']);
                        line.set_line_doctor(patient_presc['doctor']);
                        line.set_line_doctor_no(patient_presc['doctor_no']);
                        line.set_line_prescription(patient_presc['prescription']);
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
            this.patient = this.patient || "";
            this.patient_no = this.patient_no || "";
            this.hospital = this.hospital || "";
            this.doctor = this.doctor || "";
            this.doctor_no = this.doctor_no || "";
            this.prescription = this.prescription || "";
            return res;
        },
        init_from_JSON: function (json) {
            var res = _super_Orderline.init_from_JSON.apply(this, arguments);
            if (json.note) {
               this.note = this.set_line_note(json.note);
            };
            if (json.patient) {
               this.patient = this.set_line_patient(json.patient);
            };
            if (json.patient_no) {
               this.patient_no = this.set_line_patient_no(json.patient_no);
            };
            if (json.hospital) {
               this.hospital = this.set_line_hospital(json.hospital);
            };
            if (json.doctor) {
               this.doctor = this.set_line_doctor(json.doctor);
            };
            if (json.doctor_no) {
               this.doctor_no = this.set_line_doctor_no(json.doctor_no);
            };
            if (json.prescription) {
               this.prescription = this.set_line_prescription(json.patient);
            };
        },
        export_as_JSON: function () {
            console.log(this.pos.get('selectedOrderline'))
            var json = _super_Orderline.export_as_JSON.apply(this, arguments);
            if (this.note) {
                json.note = this.get_line_note();
            };
            if (this.patient) {
                json.patient = this.get_line_patient();
            };
            if (this.patient_no) {
               json.patient_no = this.get_line_patient_no();
            };
            if (this.hospital) {
               json.hospital = this.get_line_hospital();
            };
            if (this.doctor) {
               json.doctor = this.get_line_doctor();
            };
            if (this.doctor_no) {
               json.doctor_no = this.get_line_doctor_no();
            };
            if (this.prescription) {
               json.prescription = this.get_line_prescription();
            };
            return json;
        },
        clone: function () {
            var orderline = _super_Orderline.clone.call(this);
            orderline.note = this.note;
            orderline.patient = this.patient;
            orderline.patient_no = this.patient_no;
            orderline.hospital = this.hospital;
            orderline.doctor = this.doctor;
            orderline.doctor_no = this.doctor_no;
            orderline.prescription = this.prescription;
            return orderline;
        },
        export_for_printing: function () {
            var receipt_line = _super_Orderline.export_for_printing.apply(this, arguments);
            receipt_line['note'] = this.note || '';
            receipt_line['patient'] = this.patient || '';
            return receipt_line;
        },
        set_line_note: function (note) {
            this.note = note;
            this.trigger('change', this);
        },
        get_line_note: function () {
            return this.note;
        },
        set_line_patient: function (patient) {
            this.patient = patient;
            this.trigger('change', this);
        },
        get_line_patient: function () {
            return this.patient;
        },
        set_line_patient_no: function (patient_no) {
            this.patient_no = patient_no;
            this.trigger('change', this);
        },
        get_line_patient_no: function () {
            return this.patient_no;
        },
        set_line_hospital: function (hospital) {
            this.hospital = hospital;
            this.trigger('change', this);
        },
        get_line_hospital: function () {
            return this.hospital;
        },
        set_line_doctor: function (doctor) {
            this.doctor = doctor;
            this.trigger('change', this);
        },
        get_line_doctor: function () {
            return this.doctor;
        },
        set_line_doctor_no: function (doctor_no) {
            this.doctor_no = doctor_no;
            this.trigger('change', this);
        },
        get_line_doctor_no: function () {
            return this.doctor_no;
        },
        set_line_prescription: function (prescription) {
            this.prescription = prescription;
            this.trigger('change', this);
        },
        get_line_prescription: function () {
            return this.prescription;
        },
    });    
    
});
