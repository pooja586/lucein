// Copyright (c) 2017, indictrans and contributors
// For license information, please see license.txt

cur_frm.fields_dict['district1'].get_query = function(doc) {
	return{
		filters:[
			['District', 'state', '=', cur_frm.doc.state1]
		]
	}
}

cur_frm.fields_dict['city1'].get_query = function(doc) {
	return{
		filters:[
			['City', 'district', '=', cur_frm.doc.district1]
		]
	}
}

