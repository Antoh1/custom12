"use strict";

odoo.define('rt_project_quotation.quote_models', function (require) {

    var models = require('point_of_sale.models');

    models.load_fields('res.company', ['street','address','street2']);




});
