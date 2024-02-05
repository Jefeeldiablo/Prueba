# gestion_inventario/models/movimiento_inventario.py
from odoo import models, fields

class MovimientoInventario(models.Model):
    _name = 'gestion_inventario.movimiento_inventario'
    _description = 'Movimiento de Inventario'

    name = fields.Char(string='Referencia', required=True)
    date = fields.Date(string='Fecha', default=fields.Date.context_today)
    movement_type = fields.Selection([('entrada', 'Entrada'), ('salida', 'Salida')],
                                     string='Tipo de Movimiento', required=True)
    quantity = fields.Float(string='Cantidad')
    producto_id = fields.Many2one('gestion_inventario.producto', string='Producto')
    state = fields.Selection([('borrador', 'Borrador'), ('confirmado', 'Confirmado'), ('completado', 'Completado')],
                             string='Estado', default='borrador', required=True)
