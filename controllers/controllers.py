# -*- coding: utf-8 -*-
# from odoo import http


# class Project-agile(http.Controller):
#     @http.route('/project-agile/project-agile', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project-agile/project-agile/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project-agile.listing', {
#             'root': '/project-agile/project-agile',
#             'objects': http.request.env['project-agile.project-agile'].search([]),
#         })

#     @http.route('/project-agile/project-agile/objects/<model("project-agile.project-agile"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project-agile.object', {
#             'object': obj
#         })
