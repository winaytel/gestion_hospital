#Modelo para las especialidades de la clínica
from odoo import models, fields

class especialidad (models.Model):
	_name = 'especialidad.prueba'
	_description = 'Especialidades del hospital'

	name = fields.Char(string="Código de la especialidad", required=True)
	nombre_especialidad = fields.Char(string="Nombre de la especialidad", required=True)
	id_doctor_especialidad = fields.Many2many('doctor.prueba',string="Relacion de doctores")