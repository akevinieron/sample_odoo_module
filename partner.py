# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many("cofficedo.session", string="Attended Sessions", readonly=True)