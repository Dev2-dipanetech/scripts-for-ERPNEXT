# Doctype : Stock Ledger Entry  : After Submit : This code updates or make new entries in Project Based Stock Doctype whenever an entry
#  is passed through Stock Ledger entry

#  Line 2-5 : To make sure that MCS Stock Reconciliation based Stock Entries are NOT CONSIDERED for this update
#  Seperate code has been written to update PBS(Project Based Stock) through Stock Reconciliation
name = doc.voucher_no[0:7]
if name == 'MATRECO':
    pass
else:
    pbs = frappe.db.get_all('Project Based Stock', fields = ['item','warehouse','project','name','stock', 'company','batch'])
    flag = 0
    for p in pbs:
        if doc.batch_no == None:    #To chose Items without batch number
            
            if (p.item == doc.item_code) and (p.project == doc.project) and (p.warehouse == doc.warehouse):
                
                
                docum = frappe.get_doc('Project Based Stock', p.name)
                docum.stock = str(float(p.stock) + float(doc.actual_qty))   # Add/Subtract of stock based on changes in SLE
                docum.last_updated = doc.posting_date
                docum.save()
                flag  = 1
                
        else:   #To chose Items with batch number
            if (p.item == doc.item_code) and (p.project == doc.project) and (p.warehouse == doc.warehouse) and (p.batch == doc.batch_no):
                docum = frappe.get_doc('Project Based Stock', p.name)
                docum.stock = str(float(p.stock) + float(doc.actual_qty))   # Add/Subtract of stock based on changes in SLE
                docum.last_updated = doc.posting_date
                docum.save()
                flag = 1
        if flag == 1:
            break
    
    
    # Incase this particular entry does not exists in the Project Based Stock Entries - A new entry is made in PBS
    if flag == 0:
        
        docu = frappe.new_doc('Project Based Stock')
        docu.project = doc.project
        docu.item = doc.item_code
        docu.company = doc.company
        docu.uom = doc.stock_uom
        docu.stock = doc.actual_qty
        docu.last_updated = doc.posting_date
        docu.warehouse = doc.warehouse
        
        docu.batch = doc.batch_no
        
        flag = 1
        docu.save()