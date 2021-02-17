#Modelo para la relación de doctores
from odoo import models, fields

class doctor (models.Model):
	_name = 'doctor.prueba'
	_description = 'Doctores del hospital'

	name = fields.Char(string="DATOS DEL/LA DOCTOR/A")
	foto = fields.Binary()
	nombre = fields.Text(string="Nombre del doctor")
	apellido = fields.Text(string="Apellido del doctor")
	cod_doctor = fields.Char(string="Código del doctor", require=True)
	id_cita = fields.One2Many('cita.prueba','id_doctor',string="Citas del doctor")
	id_especialidad = fields.Many2many('especialidad.prueba',string="Código de especialidad", require=True)
	celular = fields.Text(string="Celular del doctor", size=9)
	n_colegiatura = fields.Char(string="Número del colegiatura del doctor", require=True)