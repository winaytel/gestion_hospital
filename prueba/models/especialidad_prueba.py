#Modelo para las especialidades de la clínica
from odoo import models, fields

class especialidad (models.Model):
	_name = 'especialidad.prueba'
	_description = 'Especialidades del hospital'

	name = fields.Char(string="ESPECIALIDADES MÉDICAS")
	cod_especialidad = fields.Many2many('doctor.prueba',string="Código", require=True)
	nombre_especialidad = fields.Text(string="Nombre de la especialidad", size=30)