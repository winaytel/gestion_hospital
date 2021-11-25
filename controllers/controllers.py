# -*- coding: utf-8 -*-
# from odoo import http


# class Gestionhospital(http.Controller):
#     @http.route('/gestionhospital/gestionhospital/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestionhospital/gestionhospital/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestionhospital.listing', {
#             'root': '/gestionhospital/gestionhospital',
#             'objects': http.request.env['gestionhospital.gestionhospital'].search([]),
#         })

#     @http.route('/gestionhospital/gestionhospital/objects/<model("gestionhospital.gestionhospital"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestionhospital.object', {
#             'object': obj
#         })
