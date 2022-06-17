from odoo import models, fields

class ProjectAgileStoryPoint(models.Model):
    _name = 'project.agile.story_point'
    _description = 'Project Agile Story Point'
    _rec_name = 'size'
    _order = 'size,description'
    size = fields.Integer('size')
    description = fields.Html('description')
    task_ids = fields.One2many('project.task', 'storypoint_id', string='Task')