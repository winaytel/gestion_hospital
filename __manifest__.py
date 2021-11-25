# -*- coding: utf-8 -*-
{
'name': "gestionhospital",

    'summary': """
        Módulo para la gestión de un hospital""",

    'description': """
        EL presente módulo es desarrollado con el fin de mostrar a los espectadores
        conceptos básicos para empezar a crear temas en Odoo.
    """,

    'author': "Wiñaytel Security",
    'website': "https://winaytel.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menusyacciones.xml',
        'views/cita_gestionhospital.xml',
        'views/doctor_gestionhospital.xml',
        'views/especialidad_gestionhospital.xml',
        'views/paciente_gestionhospital.xml',
        'views/registroclinico_gestionhospital.xml',
        'views/sala_gestionhospital.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
