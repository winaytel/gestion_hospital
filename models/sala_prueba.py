from odoo import models, fields

class sala (models.Model):
	_name = 'sala.prueba'
	_description = 'Salas del hospital'

	name = fields.Char(string="Número de la sala", required=True)
	ubicacion = fields.Text(string="Ubicación detallada de la sala")
	id_cita_sala = fields.One2many('cita.prueba','id_sala',string="Citas de la sala")