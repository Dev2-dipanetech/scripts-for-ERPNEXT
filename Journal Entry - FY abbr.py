#Ref DocType : Journal Entry   Doctype Event : Before Insert    : This is to create the correct data for the fiscal year (examples given below)  


import frappe
from frappe import doc




date = str(frappe.utils.getdate(doc.posting_date))
month =date[5:7]
year = date[2:4]
year_full = date[0:4]   
year_next = str(int(year_full) + 1)
if (int(month) > 3):
    doc.fiscal_year_abbr = year                                 # ex: output = 22
    doc.new_fy = year_full + '-' + year_next                    # ex: output = 2022-2023
else:
    doc.fiscal_year_abbr = (str(int(year) - 1))                 # ex: output = 21
    doc.new_fy = (str(int(year_full) - 1)) + '-' + year_full    # ex: output = 2021-2022
