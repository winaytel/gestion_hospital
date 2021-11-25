from odoo import models, fields

class cita(models.Model):
	_name = 'cita.gestionhospital'
	_description = 'Relacion de las citas del hospital'

	name = fields.Char(string="Código de la cita",required=True)
	cod_cita = fields.Many2one('doctor.gestionhospital',string="Código del doctor",required=True)
	id_sala = fields.Many2one('sala.gestionhospital',string="Número de la sala",required=True)
	id_paciente_cita = fields.Many2one('paciente.gestionhospital',string="DNI del paciente",required=True)
	fecha = fields.Date(string="Fecha de la cita", required=True)
	especialidad = fields.Text(string="Especialidad")
