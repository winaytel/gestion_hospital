from odoo import models, fields

class paciente (models.Model):
	_name = 'paciente.prueba'
	_description = 'Pacientes del hospital'

	name = fields.Char(string="SALA DE ATENCIÓN")
	dni = fields.Char(string="Código del paciente", require=True, size=8)
	nombre = fields.Text(string="Nombre del paciente")
	apellido = fields.Text(string="Apellido del paciente")
	fec_nac = fields.Date(string="Fecha de nacimiento del paciente")
	celular = fields.Text(string="Celular del paciente", size=9)
	id_cita = fields.One2many('cita.prueba','id_paciente',string="Citas del paciente")
	id_registroclinico = fields.One2many('registroclinico.prueba','id_paciente', string="registro clinico del paciente")