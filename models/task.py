from odoo import fields, models
class Task(models.Model):
    _inherit = 'project.task'
    story_point_id = fields.Many2one('project.agile.story_point', string='Story Point')