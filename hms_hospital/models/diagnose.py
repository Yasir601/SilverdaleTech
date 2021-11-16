# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalDiagnose(models.Model):
    _name = "hospital.diagnose"

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    notes = fields.Text(string='Description')
    patient_id = fields.Many2one('hospital.patient')
    symptoms_ids = fields.Many2many('hospital.symptom')
    treatment_ids = fields.Many2many('hospital.treatment')
    age = fields.Integer(string='Age', related="patient_id.age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True, default='male')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancelled')],
                             default='draft', string='Status')

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.onchange('patient_ids')
    def onchange_patient_ids(self):
        if self.patient_ids:
            if self.patient_ids.gender:
                self.gender = self.patient_ids.gender
        else:
            self.gender = ''


class HospitalSymptom(models.Model):
    _name = "hospital.symptom"

    name = fields.Char(string='Name')
    note = fields.Text(string='Description')
    diagnosis_ids = fields.Many2many('hospital.diagnose')


class HospitalTreatment(models.Model):
    _name = "hospital.treatment"

    name = fields.Char(string='Name')
    note = fields.Text(string='Description')
    products_ids = fields.Many2many('product.template')
    diagnosis_ids = fields.Many2many('hospital.diagnose')


class HospitalProduct(models.Model):
    _inherit = "product.template"

    treatment_ids = fields.Many2many('hospital.treatment')
