# Copyright (c) 2013, wayzon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DirectPurchase(Document):
	def on_submit(self):
		for d in self.get('item_details'):
			query=frappe.db.sql("""select * from `tabStock` where warehouse=%s and brand=%s and item=%s""",(self.warehouse,d.brand,d.item));
			if query:
				query1=frappe.db.sql("""update `tabStock` set quantity=quantity+%s  where warehouse=%s and brand=%s and item=%s""",(d.quantity,self.warehouse,d.brand,d.item));
			else:
				q=frappe.db.sql("""select max(name) from `tabStock`""")[0][0]
				if q:
					name=int(q)+1;
				else:
					name=0	
				query1=frappe.db.sql("""insert into `tabStock` set name=%s,warehouse=%s,warehouse_name=%s,brand=%s,brand_name=%s,item=%s,item_name=%s,quantity=%s""",(name,self.warehouse,self.warehouse_name,d.brand,d.brand_name,d.item,d.item_name,d.quantity));	
	pass
@frappe.whitelist()
def get_item_info(item):
	query=frappe.db.sql("""select item_name from `tabAdd Item` where  name=%s""",item)
	return query[0][0]	
