# Modelo para la relación de doctores
from odoo import models, fields

class doctor (models.Model):
    _name = 'doctor.prueba'
    _description = 'Doctores del hospital'

    name = fields.Char(string="Código del doctor", required=True)
    id_especialidad = fields.Many2many('especialidad.prueba',string="Código de la especialidad")
    foto = fields.Binary()
    nombre = fields.Text(string="Nombre")
    apellido = fields.Text(string="Apellido")
    celular = fields.Char(string="Celular", size=9)
    n_colegiatura = fields.Char(string="Número de colegiatura")
    id_cita = fields.One2many('cita.prueba', 'id_doctor', string="Citas del doctor")
    