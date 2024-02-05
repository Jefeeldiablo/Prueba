# gestion_inventario/__manifest__.py
{
    'name': 'Gestión de Inventario',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/producto_view.xml',
        'views/movimiento_inventario_view.xml',
        'workflow/movimiento_inventario_workflow.xml',
        'reports/productos_report.xml',
    ],
    'installable': True,
    'auto_install': False,
}
