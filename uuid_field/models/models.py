# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AddFieldUuidPurchase(models.Model):

	_inherit = 'purchase.order'

	field_uuid_purchase = fields.Char( string = 'Campo Uuid' )