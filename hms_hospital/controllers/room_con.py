from odoo import http
from odoo.http import request


class Room(http.Controller):

    @http.route('/room_webform', type="http", auth='public', website=True)
    def room_form(self, **kw):
        print("Execution here........................")
        return request.render('hms_hospital.room_page', {})

    @http.route('/create/webroom', type="http", auth='public', website=True)
    def create_room_record(self, **kw):
        print("Data Recieved...........")
        rec_dict = {
            'name': kw.get('name', False),
            'room_no': kw.get('room_no'),
            'room_type': kw.get('room_type'),
            'status': kw.get('status')
        }
        request.env['hospital.room'].sudo().create(rec_dict)
        return request.render('hms_hospital.room_thanks', {})

    @http.route('/delete/webroom', type="http", auth='public', website=True)
    def _delete_room_record(self, **post):
        find_id = request.env['hospital.room'].search(
            [('name', '=', post.get('name'))]).unlink()  # result demo.demo(1,)
        return request.render("hms_hospital.room_delete_thanks")

# room_val = {
#     'name': kw.get('name'),
#     'room_no': kw.get('room_no'),
#     'room_type': kw.get('room_type'),
#     'status': kw.get('status')
# }
