cur_frm.cscript.taxes=function(doc,cdt,cdn){
	var d=locals[cdt][cdn];
	var dis=d.discount/100;
	var rate=parseFloat(d.rate)-parseFloat(d.rate*dis);
	var tax=d.taxes/100;
	var price=parseFloat(rate)+parseFloat(d.rate*tax);
	var tp=price*d.quantity;
	d.price=price;
	d.amount=tp;
	refresh_field("item_details");
}
cur_frm.cscript.brand=function(doc,cdt,cdn){
	var d=locals[cdt][cdn];
	frappe.call({
		method:"purchase.purchase.doctype.material_request.material_request.get_brand_name",
		args:{brand:d.brand},
		callback:function(r){
			d.brand_name=r.message;
			refresh_field("item_details");
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
cur_frm.cscript.date=function(doc,cdt,cdn){
	var d=doc.item_details;
	var len=d.length;
	var total=0;
	for(i=0;i<len;i++)
	{
		total=parseFloat(total)+parseFloat(d[i].amount);
	}
	cur_frm.set_value("total",total);
}
