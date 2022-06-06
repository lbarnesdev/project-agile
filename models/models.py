# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class project-agile(models.Model):
#     _name = 'project-agile.project-agile'
#     _description = 'project-agile.project-agile'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
