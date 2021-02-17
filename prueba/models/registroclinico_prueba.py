from odoo import models, fields

class registro_clinico (models.Model):
	_name = 'registroclinico.prueba'
	_description = 'Registro clínico de los pacientes del hospital'

	name = fields.Char(string="REGISTRO CLÍNICO")
	cod_registro = fields.Char(string="Código del registro")
	id_paciente = fields.Many2one('paciente.prueba',string="Datos del paciente")
	diagnostico = fields.Text(string="Diagnóstico del paciente")
	receta = fields.Text(string="Receta del paciente")
	examen = fields.Text(string="Examen a realizar")