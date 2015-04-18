# Copyright (c) 2013, Wayzon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MaterialRequest(Document):
	#def on_submit(self):
	#query=frappe.db.sql("""update `tabMaterial Request` set status=%s""",'Purchased')
	pass
@frappe.whitelist()
def get_brand_name(brand):
	query=frappe.db.sql(""" select brand_name from `tabAdd Brand` where name=%s""",(brand))
	brand_name=str(query[0][0])
	return brand_name
@frappe.whitelist()
def get_item_name(item):
	query=frappe.db.sql("""select item_name from `tabAdd Item` where name=%s""",(item))
	item_name=str(query[0][0])
	return item_name			

