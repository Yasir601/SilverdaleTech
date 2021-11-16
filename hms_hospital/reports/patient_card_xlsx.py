from odoo import models
import base64
import io


class PatientCardXlsx(models.AbstractModel):
    _name = 'report.hms_hospital.report_patient_id_card_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        sheet = workbook.add_worksheet('Patient ID Card')
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': 'yellow'})

        row = 3
        col = 3
        sheet.set_column('D:D', 15)
        sheet.set_column('E:E', 15)

        for obj in patients:
            row = row + 1
            sheet.merge_range(row, col, row, col + 1, 'Patient Details', format_1)

            row = row + 1
            if obj.image:
                product_image = io.BytesIO(base64.b64decode(obj.image))
                sheet.insert_image(row, col, "image.png", {'image_data': product_image, 'x_scale': 0.4, 'y_scale': 0.4})

                row = row + 5

            row = row + 1
            sheet.write(row, col, 'Name', bold)
            sheet.write(row, col + 1, obj.name)
            row = row + 1
            sheet.write(row, col, 'Father Name', bold)
            sheet.write(row, col + 1, obj.father_name)
            row = row + 1
            sheet.write(row, col, 'Age', bold)
            sheet.write(row, col + 1, obj.age)
