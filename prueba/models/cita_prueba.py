from odoo import models, fields

class cita (models.Model):
	_name = 'cita.prueba'
	_description = 'Citas del hospital'

	name = fields.Char(string="Detalles de la cita")
	cod_cita = fields.Char(string="Código de la cita", require=True)
	id_doctor = fields.Many2one('doctor.prueba',string="Código del doctor", require=True)
	id_sala = fields.Many2one('sala.prueba',string="Número de la sala", require=True)
	id_paciente = fields.Many2one('paciente.prueba', string="DNI del paciente", require=True)
	fecha = fields.Date(string="Fecha de la cita",require=True)
	especialidad = fields.Text(string="Nombre de la specialidad")

