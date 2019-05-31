# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from xml.dom import minidom
from suds.client import Client
import tempfile
import base64
import os
from odoo.exceptions import ValidationError, UserError
from xml.etree import ElementTree as ET

class AddFieldUuidPurchase(models.Model):

	_inherit = 'purchase.order'

	@api.multi
	def verific(self):
		self.ensure_one()
		return self.env['ir.attachment'].search([('res_name', '=', self.name)], limit=1)

	@api.multi
	def test(self):
		for invoice in self:
			test = invoice.verific()
			if test:
				xml = test.datas
				self.field_uuid_purchase = 1
			else:
				self.field_uuid_purchase = 2

	field_uuid_purchase = fields.Char( string = "Campo Uuid" )

	upload_field_uuid = fields.Binary( string = "Campo UUID" )

	@api.onchange('upload_field_uuid')
	def fieldUuid(self):
		if self.upload_field_uuid:
			data = base64.b64encode(bytes(self.upload_field_uuid,'utf-8'))
			#data2 = base64.decodestring(self.upload_field_uuid)
			fObject = tempfile.NamedTemporaryFile( delete = False )
			print("****** TEST1 " + str(fObject))
			fName = fObject.name
			fObject.write(data)
			fObject.close()
			fileRec = open(fName, "r")
			fName = fName.encode('utf-8')
			print("***** TEST2 " + str(fileRec))
			self.field_uuid_purchase = fName



class AddFieldUuidExpenses(models.Model):

	_inherit = 'hr.expense'

	field_uuid_expenses = fields.Char( string = 'Campo Uuid' )