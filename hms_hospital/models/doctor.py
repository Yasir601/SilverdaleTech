# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctor"

    name = fields.Char(string='Name', required=True)
    age = fields.Char(string='Age')
    specialization = fields.Char(string='Specialization', required='True')
    phone_no = fields.Char(string='Phone Number')
    image = fields.Binary(string='image')
    address = fields.Char(string='Address')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True, default='male')
    patient_ids = fields.Many2many('hospital.patient')
    notes = fields.Text(string='Description')
    user_id = fields.Many2one('res.users')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancelled')],
                             default='draft', string='Status')

    def action_confirm(self):
        self.state = 'confirm'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Doctor Appointment Confirm',
                'type': 'rainbow_man',
            }
        }

    @api.model
    def test_cron_job(self):
        print('Check Doctor Status Here...')

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

