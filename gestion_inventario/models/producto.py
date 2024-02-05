# gestion_inventario/models/producto.py
from odoo import models, fields

class Producto(models.Model):
    _name = 'gestion_inventario.producto'
    _description = 'Producto'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    price = fields.Float(string='Precio')
    stock_quantity = fields.Float(string='Cantidad en Stock')
