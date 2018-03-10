# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Course(models.Model):
    _name = 'cofficedo.course'

    name = fields.Char(string="Titulo", required=True)
    description = fields.Text()
    capacity = fields.Integer()

    responsible_id = fields.Many2one("res.users", ondelete="set null", string="Responsible", index=True)
    session_ids = fields.One2many("cofficedo.session", "course_id", string="Sessions")

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [("name", "=like", u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

    _sql_constraints = [
        ("name_description_check",
         "CHECK(name != description)",
         "The title of the course should not be the description"),

        ("name_unique",
         "UNIQUE(name)",
         "The course title must be unique"),
    ]


class Session(models.Model):
    _name = 'cofficedo.session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)

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

    @api.onchange("seats", "attendee_ids")
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                "warning": {
                    "title" : "Incorrect 'seats' value",
                    "message": "The number of available seats may not be negative"
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                "warning": {
                    "title": "Too many attendees",
                    "message": "Increase seats or remove excess attendees"
                },
            }

    @api.constrains("instructor_id", "attendee_ids")
    def _check_instructor_not_in_attendees(self):
        for record in self:
            if record.instructor_id and record.instructor_id in record.attendee_ids:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")

