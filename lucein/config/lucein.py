from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"items": [
				{
					"type": "doctype",
					"name": "Planning",
					"description": _("Database of Planning."),
				},
				{
					"type": "doctype",
					"name": "Daily Activity",
					"description": _("Database of Daily Activity."),
				},
			
			]
		},
		{
			"label": _("Masters"),
			"items": [
				{
					"type": "doctype",
					"name": "Item",
					"description": _("Database of Item."),
				},
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Database of Customer."),
				},
				{
					"type": "doctype",
					"name": "Address",
					"description": _("Database of Address."),
				},
				{
					"type": "doctype",
					"name": "Employee",
					"description": _("Database of Employee."),
				},
				{
					"type": "doctype",
					"name": "Country",
					"description": _("Database of Country."),
				},
				{
					"type": "doctype",
					"name": "State",
					"description": _("Database of State."),
				},
				{
					"type": "doctype",
					"name": "District",
					"description": _("Database of District."),
				},
				{
					"type": "doctype",
					"name": "City",
					"description": _("Database of City."),
				},
				{
					"type": "doctype",
					"name": "Company Branch",
					"description": _("Database of Company Branch."),
				},

				
			]
		},
		
	]