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

    length = fields.Char(string="Length", store=True)
    width = fields.Char(string="Width", store=True)
    quantity_sqm = fields.Char(string="Piece(s)", store=True)

    def _order_line_fields(self, line, session_id=None):
        res = super(PosOrderLine, self)._order_line_fields(line, session_id=None)
        if line and 'patient' in line[2]:
            res[2]['length'] = line[2]['length'] if line[2]['length'] else False
            res[2]['width'] = line[2]['width'] if line[2]['width'] else False
            res[2]['quantity_sqm'] = line[2]['quantity_sqm'] if line[2]['quantity_sqm'] else False
        return res
