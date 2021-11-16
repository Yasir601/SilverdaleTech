{
    'name': 'Hospital',
    'version': '14.0.1.0.0',
    'summary': 'Hospital Application Software',
    """
    The module is about that all details of hospital Management stores inside it Patients, Doctors, Appointment,
    Bill details are store inside it.
    """
    'sequence': -100,
    'author': 'Silverdale',
    'description': """
    The module is about Hospital Management System in which patients can take online appointment from the the doctors,
    all The patients can easily search doctors and take appointment all tha data stores inside.
    """,
    'category': 'CRM',
    'website': 'https://www.silverdaletech.com/',
    'license': 'LGPL-3',
    'depends': [
        'mail',
        'sale',
        'account',
        'report_xlsx'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/data.xml',
        'data/cron.xml',
        'wizard/create_bill_view.xml',
        'views/patients.xml',
        'views/doctor.xml',
        'views/diagnose.xml',
        'views/room.xml',
        'views/labotary.xml',
        'views/bill.xml',
        'views/res_partner.xml',
        'views/template.xml',
        'views/room_temp_con.xml',
        'reports/report.xml',
        'reports/patient_card_report.xml',
        'reports/bill_details.xml',
        'views/menu.xml'

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
