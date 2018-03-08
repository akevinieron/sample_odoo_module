# -*- coding: utf-8 -*-
{
    'name': "cofficedo",

    'summary': """
        The CofficeDO Description This is the summary""",

    'description': """
        The CofficeDO Long description of module
    """,

    'author': "Kevin Jimenez",
    'website': "http://kevin.do",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/cofficedo.xml',
        'views/partner.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}