from odoo import models, fields


class paciente (models.Model):
    _name = 'paciente.prueba'
    _description = 'Pacientes del hospital'

    name = fields.Char(string="DNI", required=True, size=8)
    nombre = fields.Char(string="Nombre")
    apellido = fields.Char(string="Apellido")
    fec_nac = fields.Date(string="Fecha de nacimiento")
    celular = fields.Char(string="Celular", size=9)
    id_cita_paciente = fields.One2many('cita.prueba', 'id_paciente_cita', string="Citas del paciente")
    id_registroclinico = fields.One2many('registroclinico.prueba', 'id_paciente_registro', string="Registro clinico del paciente")
