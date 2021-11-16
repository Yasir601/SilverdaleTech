# -*- coding: utf-8 -*-
from odoo import api, fields, models


class hospital_Labotary(models.Model):
    _name = "hospital.labotary"

    name = fields.Char(String='Laboratory Name', required=True)
    test_type = fields.Char(string='Test Type')
    patient_ids = fields.Many2many('hospital.patient')
    doctor_id = fields.Many2one('hospital.doctor')
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
