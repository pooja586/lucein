# -*- coding: utf-8 -*-
# Copyright (c) 2017, sagar.s@indictranstech.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import cstr, flt, getdate, comma_and, cint, nowdate
from frappe.model.document import Document

class Planning(Document):
	def validate(self):
		self.validate_date()
		if self.status == "Approved":
			self.send_approved_planning_notifcation()
	
	def validate_date(self):
		if getdate(self.start_date) > getdate(self.end_date):
			frappe.throw(("Start date ahead of end date"))
	
	def send_approved_planning_notifcation(self):
		name=frappe.db.get_value("User",{"name":self.plan_owner},"first_name")
		frappe.sendmail(
				recipients = self.plan_owner,
				sender = frappe.session.user,
				subject = "Approved Planning Notification For Plan "+self.name ,
				message = frappe.render_template("templates/email/send_approved_planning_notifcation.html", {"Name":name,"plan": self.name}) 
		)

@frappe.whitelist()
def get_permission_query_conditions(user):
	# pass
	if not user: user = frappe.session.user

	roles = frappe.get_roles(user)
	if user == "Administrator":
		return ""
	else:
		if "Sales Executive" in roles:
			return """(`tabPlanning`.owner='{user}')""".format(user=user)
		elif "S Manager" in roles:
			return """(`tabPlanning`.owner in (select distinct reference_name as owner from tabToDo where 
				  reference_type='User' and owner = '{0}'))""".format(user)

