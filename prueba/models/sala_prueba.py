from odoo import models, fields

class sala (models.Model):
	_name = 'sala.prueba'
	_description = 'Salas del hospital'

	name = fields.Char(string="SALA DE ATENCIÓN")
	n_sala = fields.Char(string="Número de la sala")
	ubicacion = fields.Text(string="Ubicación detallada de la sala")
	id_cita = fields.One2many('cita.prueba','id_sala',string="Citas de la sala")