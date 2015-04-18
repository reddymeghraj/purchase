cur_frm.cscript.brand=function(doc,cdt,cdn)
{
	var d=locals[cdt][cdn];
		 frappe.call({
			method:"purchase.purchase.doctype.material_request.material_request.get_brand_name",
			args:{ "brand" : d.brand },
			callback: function(r) {
				d.brand_name = r.message;
				refresh_field('item_details');
			}
		});
}
cur_frm.cscript.item=function(doc,cdt,cdn){
	var d=locals[cdt][cdn];
	frappe.call({
		method:"purchase.purchase.doctype.material_request.material_request.get_item_name",
		args:{item:d.item},
		callback:function(r){
			d.item_name = r.message;
			refresh_field('item_details');
		}
	});
}