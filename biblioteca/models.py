# -*- coding: utf-8 -*-

##############################################################################

#

#    OpenERP, Open Source Management Solution

#    Copyright (C) 2015 S&C (<http://salazarcarlos.com>).

#

#    This program is free software: you can redistribute it and/or modify

#    it under the terms of the GNU Affero General Public License as

#    published by the Free Software Foundation, either version 3 of the

#    License, or (at your option) any later version.

#

#    This program is distributed in the hope that it will be useful,

#    but WITHOUT ANY WARRANTY; without even the implied warranty of

#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

#    GNU Affero General Public License for more details.

#

#    You should have received a copy of the GNU Affero General Public License

#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#

##############################################################################



from __manifest__ import models, fields, api, _


class biblioteca_libro(models.Model):

    _name = 'biblioteca.libro'

    name = fields.Char(string='Titulo', required=True,)

    description = fields.Text('Observacion')

    date = fields.Date(string='Fecha de registro')
    
    
    class Autor(models.Model):
        
        _inherit = "biblioteca.libro"
        _name = "autor"
        nombre = fields.Char(string="Nombre autor", required= True)
        primer_apellido = fields.Char(string="primer Apellido", required=True)
        segundo_apellido = fields.Char(string='Segundo Apellido', required=True)
        edad = fields.Integer(string="edad")
        fecha_nacimiento= fields.Date(string="fecha_nacimiento")
        genero = fields.Selection([('h', 'hombre'), ('m', 'mujer'), ('o', 'otro')], string='genero')
        nacionalidad = fields.Many2one('res.country', string='nacionalidad')
    