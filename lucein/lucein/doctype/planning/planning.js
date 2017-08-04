// Copyright (c) 2017, sagar.s@indictranstech.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Planning', {

	onload:function(frm){
		if(frm.doc.__islocal == 1){
			cur_frm.set_value("plan_owner",user)
		}					 
	},

	refresh: function(frm){
		if(frm.doc.workflow_state == "Rejected") {
			cur_frm.set_value("status","Cancel")
		}
		else{
			cur_frm.set_value("status",frm.doc.workflow_state)
		}
	
	},

	validate(frm){
	
	}
});
