# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CreateBillWizard(models.TransientModel):
    _name = "create.bill.wizard"

    patient_id = fields.Many2one('hospital.patient')
    bill_no = fields.Integer(String='Bill No', required=True)
    doctor_charge = fields.Integer(String='Doctor Charges')
    room_charge = fields.Integer(String='Room Charges')
    no_of_days = fields.Integer(string='Number of Days')
    lab_charge_bill = fields.Integer(string='Lab Charge Bills')
    notes = fields.Text(string='Description')

    def action_print_report(self):
        # lab_charge_bill = self.env['hospital.bill'].search_read([])
        # 'lab_charge_bill': lab_charge_bill
        data = {}
        return self.env.ref('hms_hospital.report_create_bill').report_action(self, data=data)

    # sub_total = fields.Monetary(string="Sub Total")


class Hospital_Bill_Invoice_wiz(models.TransientModel):
    _name = "hospital.bill.invoice.wiz"
    _rec_name = "owner_id"

    owner_id = fields.Many2one('res.partner')
    date = fields.Date(string='Invoice Date')
    due_date = fields.Date(string='Due Date')
    payment = fields.Char(string='Payment')

    def create_invoice(self):
        return self.env['account.move'].create({
            'partner_id': self.owner_id.id,
            'invoice_date': self.date,
            'invoice_date_due': self.due_date,
            'move_type': 'out_invoice',
            'payment_reference': self.payment
        })

# def generate_invoice(self):
#     return self.env['account.move'].create({
#         'partner_id': self.owner_id.id,
#         'invoice_date': self.date,
#         'invoice_date_due': self.due_date,
#         'move_type': 'out_invoice',
#         'payment_reference': self.payment
#     })

# owner_id = fields.Many2one('res.partner')
# date = fields.Date(string='Invoice Date')
# due_date = fields.Date(string='Due Date')
# payment = fields.Char(string='Payment')
