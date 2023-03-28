{
    'name': 'CRM Commission',
    'version': '16.0.1.0.0',
    'summary': 'Commission plan',
    'sequence': -4,
    'installable': True,
    'application': True,

    'depends': ['base', 'product', 'crm', 'sale', 'mail'],
    'data': ['security/ir.model.access.csv',
             'views/crm_commission_views.xml',
             'views/crm_team_views.xml',
             'views/sale_order_line_views.xml'
             ]
}
