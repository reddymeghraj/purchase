# Copyright (c) 2013, wayzon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Pinvoice(Document):
	pass
@frappe.whitelist()
def get_item_info(item,brand,po):
	query=frappe.db.sql("""select item_name,quantity,rate,discount,taxes,price,amount from `tabPo Details` where parent=%s and brand=%s and item=%s""",(po,brand,item),as_dict=1)
	return query