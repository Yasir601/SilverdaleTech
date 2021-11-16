# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth and record.date_of_birth <= fields.Date.today():
                record.age = relativedelta(
                    fields.Date.from_string(fields.Date.today()),
                    fields.Date.from_string(record.date_of_birth)).years
            else:
                record.age = 0

    """
    This function work when we type the name of the patient generate his id automatically. 
    Means auto change id of the patients, In python odoo its called sequential field. 
    """

    @api.model
    def create(self, vals):
        if vals.get('p_id', _('New')) == _('New'):
            vals['p_id'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
            result = super(HospitalPatient, self).create(vals)
            return result

    name = fields.Char(string='Name', track_visibility='onchange', required="True")
    father_name = fields.Char(string='Father_Name')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age')
    p_id = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    phone_no = fields.Char(string='Phone Number')
    date_of_admit = fields.Date(string='Admit Date')
    date_of_discharge = fields.Date(string='Discharge Date')
    phone_no = fields.Char(string='Phone Number')
    email_id = fields.Char(string='Email')
    address = fields.Char(string='Address')
    blood_group = fields.Char(string='Blood Group')
    normal_abnormal = fields.Boolean(string='Normal or Abnormal')
    image = fields.Binary("Patient Image")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True, default='male')
    doctor_ids = fields.Many2many('hospital.doctor')
    laboratory_id = fields.Many2one('hospital.labotary')
    room_id = fields.Many2one('hospital.room')
    diagnosis_ids = fields.One2many('hospital.diagnose', 'patient_id')
    responsible_id = fields.Many2one('res.partner')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancelled')],
                             default='draft', string='Status')
    user_id = fields.Many2one('res.users')
    active = fields.Boolean('Active', default=True)
    doctor_count = fields.Integer(string="Doctor Count", compute='compute_doctor_count')
    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.user.company_id)
    notes = fields.Text(string='Description')

    """
    This is compute function This function depends on another fields whenever call this function,
     its count all the doctor which is assign to patients.
    """

    def compute_doctor_count(self):
        count = self.env['hospital.doctor'].search_count([('patient_ids', '=', self.ids)])
        self.doctor_count = count

    """
     Name get function is used to add a field to name when this function call the id is add to name of the patient......
     """

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.p_id, rec.name)))
        return res

    """
     Whenever call this function it's print the report of patient......
     """

    def print_report(self):
        return self.env.ref('hms_hospital.report_patient_card').report_action(self)

    """
     Whenever call this function the stage is changed to Confirm state......
     """

    def action_confirm(self):
        self.state = 'confirm'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Patient Confirm',
                'type': 'rainbow_man',
            }
        }

    """
    Whenever call this function the stage is changed to done state......
    """

    def action_done(self):
        self.state = 'done'

    """
    Whenever call this function the stage is changed to draft state......
    """

    def action_draft(self):
        self.state = 'draft'

    """
    Whenever call this function it's goes to cancel state ......
    """

    def action_cancel(self):
        self.state = 'cancel'

    """
    Whenever call this function it goes to the doctor models and return those doctor which is assign to patients  ......
    """

    def get_doctor_action(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Doctors',
            'view_mode': 'tree,form',
            'res_model': 'hospital.doctor',
            'domain': [('patient_ids', '=', self.ids)],
            'target': 'current',
        }
