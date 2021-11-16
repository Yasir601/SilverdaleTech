from odoo import http
from odoo.http import request


class Hospital(http.Controller):
    @http.route('/hospital/patient/', auth='public', website=True)
    def hospital_patient(self, **kwargs):
        patient_details = request.env['hospital.patient'].sudo().search([])
        return request.render('hms_hospital.patients_page', {'my_details': patient_details})

    #
    # my_details = []
    # for patient in my_details:
    #     patient_dic = {
    #         'name': patient.name,
    #         'father_name': patient.father_name,
    #         'age': patient.age,
    #         'state': patient.state,
    #     }
    #     my_details.append(patient_dic)
    #     values = {
    #         'my_details': my_details,
    #     }
    #     return request.render('hms_hospital.patients_page', values)
