# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'cofficedo.course'

    name = fields.Char(string="Titulo", required=True)
    description = fields.Text()
    capacity = fields.Integer()

    responsible_id = fields.Many2one("res.users", ondelete="set null", string="Responsible", index=True)
    session_ids = fields.One2many("cofficedo.session", "course_id", string="Sessions")


class Session(models.Model):
    _name = 'cofficedo.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=["|", ("instructor","=",True),("category_id.name", "ilike", "Teacher")])
    course_id = fields.Many2one('cofficedo.course', ondelete="cascade", string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    taken_seats = fields.Float(string="Taken seats", compute="_taken_seats")

    @api.depends("seats", "attendee_ids")
    def _taken_seats(self):
        for record in self:
            if not record.seats:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100 * len(record.attendee_ids) / record.seats

