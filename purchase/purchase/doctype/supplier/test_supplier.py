# Copyright (c) 2013, Wayzon and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Supplier')

class TestSupplier(unittest.TestCase):
	pass
