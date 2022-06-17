# -*- coding: utf-8 -*-
{
    'name': "project-agile",

    'summary': """
        modify project to fit an agile project kanban""",

    'description': """
        modify project to fit an agile project kanban
    """,

    'author': "Good Medicine Solutions",
    'license': "OPL-1",
    'website': "https://www.barnesfam.us",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Library/Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/story_point_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
