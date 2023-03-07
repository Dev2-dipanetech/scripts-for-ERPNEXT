# Doctype: MCS Stock Reconciliation : After Save : This code makes(may not make, depending on condition) new stock entries whenever 
# MCS Stock Reco is submitted

for d in doc.get("items"):
    if(d.qty - d.current_qty) < 0:   #If the difference is negative, a Materail Issue based stock entry is passed
        # frappe.throw("check")
        docu = frappe.new_doc('Stock Entry')
        docu.stock_entry_type = 'Material Issue'
        docu.stock_reconciliation = doc.name
        docu.company = doc.company
        docu.set_posting_time = 1   # To check the option for editing stock entry posting_date and time
        docu.naming_series = 'MATRECO-.company_abbreviation.-.######'
        docu.posting_date = doc.posting_date
        docu.posting_time = doc.posting_time
        docu.company_abbreviation = doc.company_abbr
        
        docu.append("items",{'item_code': d.item_code,'s_warehouse': d.warehouse,'qty': (d.current_qty - d.qty),'project': d.project,'uom': frappe.get_doc('Item',d.item_code).stock_uom,'stock_uom': frappe.get_doc('Item',d.item_code).stock_uom,	'conversion_factor': 1,	'batch_no': d.batch, 'expense_account': '411-40 - Stock Adjustment - MCS'})
        docu.insert()
        docu.save()
        docu.submit()
    if (d.qty - d.current_qty) > 0:     #If the difference is positive, a Materail Reciept based stock entry is passed
        doc2 = frappe.new_doc('Stock Entry')
        doc2.stock_entry_type = 'Material Receipt'
        doc2.naming_series = 'MATRECO-.company_abbreviation.-.######'
        doc2.stock_reconciliation = doc.name
        doc2.company = doc.company
        doc2.set_posting_time = 1
        doc2.posting_date = doc.posting_date
        doc2.posting_time = doc.posting_time
        doc2.company_abbreviation = doc.company_abbr
        doc2.append("items",{'item_code': d.item_code,'t_warehouse': d.warehouse,'qty': (d.qty - d.current_qty),'project': d.project,'uom': frappe.get_doc('Item',d.item_code).stock_uom,'stock_uom': frappe.get_doc('Item',d.item_code).stock_uom,	'conversion_factor': 1,	'batch_no': d.batch, 'expense_account': '411-40 - Stock Adjustment - MCS'})
        doc2.insert()
        doc2.save()
        doc2.submit()  