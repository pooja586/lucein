// Copyright (c) 2017, indictrans and contributors
// For license information, please see license.txt

cur_frm.fields_dict['company_branch'].get_query = function(doc) {
	return{
		filters:[
			['Company Branch', 'Company', '=', cur_frm.doc.company]
		]
	}
}