// Copyright (c) 2017, sagar.s@indictranstech.com and contributors
// For license information, please see license.txt
// Copyright (c) 2017, indictrans technologies and contributors
// For license information, please see license.txt

cur_frm.add_fetch('contact','mobile_no','contact_mobile_no')
cur_frm.add_fetch('contact','email_id','contact_email')

frappe.ui.form.on('Daily Activity', {

	onload: function(frm) {
		if(frm.doc.__islocal == 1){
			cur_frm.set_value("dsr_owner",frappe.session.user)
		}
		if (!frm.doc.date) {
   			frm.set_value("date", get_today());
   		}
	},
	refresh: function(frm) {
		frm.add_custom_button(__('Close'), function() {
			frappe.set_route("List", "Daily Activity")	
		})
	}
});

cur_frm.fields_dict['contact'].get_query = function(doc) {
	return {
		query: "lucien.lucien_tech.doctype.daily_activity.daily_activity.get_contact_details",
		filters: {
			"customer" : cur_frm.doc.customer
		}
	}
}