# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lucein"
app_title = "lucein"
app_publisher = "sagar.s@indictranstech.com"
app_description = "Book Publication"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sagar.s@indictranstech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lucein/css/lucein.css"
# app_include_js = "/assets/lucein/js/lucein.js"

# include js, css files in header of web template
# web_include_css = "/assets/lucein/css/lucein.css"
# web_include_js = "/assets/lucein/js/lucein.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "lucein.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "lucein.install.before_install"
# after_install = "lucein.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lucein.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
permission_query_conditions = {
	"Customer": "lucein.custom_script.customer.customer.get_permission_query_conditions",
	"Planning":"lucein.lucein.doctype.planning.planning.get_permission_query_conditions"
	# "Contact": "lucien.py.contact.get_permission_query_conditions"
}
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doctype_js={
	"Address":["custom_script/address/address.js"],
	"Employee":["custom_script/employee/employee.js"]
}

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"lucein.tasks.all"
# 	],
# 	"daily": [
# 		"lucein.tasks.daily"
# 	],
# 	"hourly": [
# 		"lucein.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lucein.tasks.weekly"
# 	]
# 	"monthly": [
# 		"lucein.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "lucein.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lucein.event.get_events"
# }

