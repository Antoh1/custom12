import logging
from datetime import timedelta
from functools import partial

import psycopg2
import pytz

from odoo import api, fields, models, tools, _
from odoo.tools import float_is_zero
from odoo.exceptions import UserError
from odoo.http import request
from odoo.addons import decimal_precision as dp

_logger = logging.getLogger(__name__)

class PosOrderLine(models.Model):
    _inherit = "pos.order.line"

    patient = fields.Char(string="Client", store=True)
    patient_no = fields.Char(string="Client Tel", store=True)
    hospital = fields.Char(string="Hospital", store=True)
    doctor = fields.Char(string="Doctor", store=True)
    doctor_no = fields.Char(string="Doctor Tel", store=True)
    prescription = fields.Char(string="Prescription", store=True)

    def _order_line_fields(self, line, session_id=None):
        res = super(PosOrderLine, self)._order_line_fields(line, session_id=None)
        if line and 'patient' in line[2]:
            res[2]['patient'] = line[2]['patient'] if line[2]['patient'] else False
            res[2]['patient_no'] = line[2]['patient_no'] if line[2]['patient_no'] else False
            res[2]['hospital'] = line[2]['hospital'] if line[2]['hospital'] else False
            res[2]['doctor'] = line[2]['doctor'] if line[2]['doctor'] else False
            res[2]['doctor_no'] = line[2]['doctor_no'] if line[2]['doctor_no'] else False
            res[2]['prescription'] = line[2]['prescription'] if line[2]['prescription'] else False
        return res
