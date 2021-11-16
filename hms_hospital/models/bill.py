# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Hospital_Bill(models.Model):
    _name = "hospital.bill"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient')
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    bill_no = fields.Integer(String='Bill No', required=True)
    doctor_charge = fields.Integer(String='Doctor Charges')
    room_charge = fields.Integer(String='Room Charges')
    no_of_days = fields.Integer(string='Number of Days')
    lab_charge_bill = fields.Integer(string='Lab Charge Bills')
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

# product = fields.Many2one(string="Product")
# name = fields.Char(string="Label")
# quantity = fields.Float(string="Quantity")
# price = fields.Float(string="Price")
# taxes_ids = fields.Many2many(string="Taxes")
# # sub_total = fields.Monetary(string="Sub Totals")
