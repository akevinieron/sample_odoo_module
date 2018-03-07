# -*- coding: utf-8 -*-
from odoo import http

# class Cofficedo(http.Controller):
#     @http.route('/cofficedo/cofficedo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cofficedo/cofficedo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cofficedo.listing', {
#             'root': '/cofficedo/cofficedo',
#             'objects': http.request.env['cofficedo.cofficedo'].search([]),
#         })

#     @http.route('/cofficedo/cofficedo/objects/<model("cofficedo.cofficedo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cofficedo.object', {
#             'object': obj
#         })