from odoo import models, fields

class cita (models.Model):
	_name = 'cita.prueba'
	_description = 'Citas del hospital'

	name = fields.Char(string="Código de la cita", required=True)
	id_doctor = fields.Many2one('doctor.prueba',string="Código del doctor")
	id_sala = fields.Many2one('sala.prueba',string="Número de la sala")
	id_paciente_cita = fields.Many2one('paciente.prueba', string="DNI del paciente")
	fecha = fields.Date(string="Fecha de la cita")
	especialidad = fields.Char(string="Especialidad")

