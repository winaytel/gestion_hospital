from odoo import models, fields

class registro_clinico (models.Model):
	_name = 'registroclinico.gestionhospital'
	_description = 'Registro clínico de los pacientes del hospital'

	name = fields.Char(string="Código del registro", required=True)
	id_paciente_registro = fields.Many2one('paciente.gestionhospital',string="DNI del paciente")
	diagnostico = fields.Text(string="Diagnóstico del paciente")
	receta = fields.Text(string="Receta del paciente")
	examen = fields.Text(string="Examen a realizar")