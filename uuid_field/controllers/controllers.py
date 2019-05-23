# -*- coding: utf-8 -*-
from odoo import http

# class UuidField(http.Controller):
#     @http.route('/uuid_field/uuid_field/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uuid_field/uuid_field/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('uuid_field.listing', {
#             'root': '/uuid_field/uuid_field',
#             'objects': http.request.env['uuid_field.uuid_field'].search([]),
#         })

#     @http.route('/uuid_field/uuid_field/objects/<model("uuid_field.uuid_field"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uuid_field.object', {
#             'object': obj
#         })