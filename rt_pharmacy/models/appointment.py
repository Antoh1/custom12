# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Appointment'
    _order = 'id desc, appointment_date desc'


    @api.model
    def create(self, vals):        # generating sequence for HospitalAppointment model
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.code') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    def _set_default_code(self):
        return "The odoo sw is the game changer in the business industry"

    name = fields.Char(string="Appointment ID", required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'), store=True)
    patient_id = fields.Many2one(comodel_name="res.partner", string="Patient", required=True, domain="[('is_patient', '=', True)]")
    doctor = fields.Many2one(comodel_name="res.partner", string="Pharmacist/Doctor", required=True,
                             domain="[('is_doctor', '=', True)]")
    patient_age = fields.Integer(string="Age")
    user_id = fields.Many2one('res.users', string='Attendant :', default=lambda self: self.env.user, tracking=True)
    patient_phone = fields.Char(related='patient_id.phone')
    notes = fields.Text(string="Appointment Details")
    illness = fields.Char('Illness', store=True)
    history = fields.Text(string="Illness History")
    prescription = fields.Text(string="Doctor Prescription")
    hospital_visits = fields.One2many('hospital.visit', 'appointment_id', string='Patient Visits')
    appointment_date = fields.Date(string="Appointment Date", store=True)


class HospitalVisit(models.Model):
    _name = 'hospital.visit'

    service = fields.Text('Services offered', store=True)
    illness = fields.Char(related='appointment_id.illness')
    doctor = fields.Many2one(comodel_name="res.partner", string="Pharmacist/Doctor", required=True, domain="[('is_doctor', '=', True)]")
    visit_date = fields.Date(string="Visit Date", store=True)
    next_visit = fields.Date(string="Next Visit", store=True)
    appointment_id = fields.Many2one(comodel_name="hospital.appointment", string='Patient Number')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_patient = fields.Boolean(string="Is Patient?", default=True)
    is_doctor = fields.Boolean(string="Is Patient?")
