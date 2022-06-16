from odoo import models, fields

class ProjectAgileStoryPoint(models.Model):
    _name = 'project.agile.story_point'
    _description = 'Project Agile Story Point'
    size = fields.Integer('size')
    description = fields.Html('description')