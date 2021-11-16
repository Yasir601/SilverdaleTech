# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    orientation_staff_id = fields.Many2one('res.users')
    patient_ids = fields.One2many('hospital.patient', 'responsible_id')

    """
    override method
    """

    @api.model
    def create(self, vals):
        rec = super(ResPartner, self).create(vals)
        print('Method override')
        return rec
