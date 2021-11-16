# -*- coding: utf-8 -*-
from odoo import api, fields, models


class hospitalRoom(models.Model):
    _name = 'hospital.room'

    name = fields.Char(string='Room Name')
    room_no = fields.Char(string='Room No')
    room_type = fields.Char(string='Room Type')
    status = fields.Char(string='Status')
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
