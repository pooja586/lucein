from __future__ import unicode_literals
import frappe



@frappe.whitelist()
def get_permission_query_conditions(user):
	# pass
	if not user: user = frappe.session.user

	roles = frappe.get_roles(user)
	if user == "Administrator":
		return ""
	else:
		if "Sales Executive" in roles:
			return """(`tabCustomer`.name in (select distinct reference_name as name 
			from tabToDo where reference_type='Customer' and owner = '{0}') or owner = '{1}' )""".format(user,user)