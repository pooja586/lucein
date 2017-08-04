# -*- coding: utf-8 -*-
# Copyright (c) 2017, indictrans technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cstr, flt, getdate, comma_and, cint, nowdate

class DailyActivity(Document):
	def validate_date(self):
		if getdate(self.next_visit) < getdate():
			frappe.throw(("Start date ahead of end date"))

@frappe.whitelist()
def get_contact_details(doctype, txt, searchfield, start, page_len, filters):
	if filters['customer']:
		contact_info = frappe.db.sql(""" select parent from `tabDynamic Link` where parenttype = "Contact" AND
								link_name = '{0}' """.format(filters['customer']),as_list=1)
		return contact_info