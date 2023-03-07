#Doctype Event : MCS Stock Reconciliation : After Submit  : This code updates the stock in the Project Based Stock, when Entries are 
# passed through MCS Stock Reconciliation


for d in doc.get("items"):
    flag = 0
    for pbs in frappe.get_all(doctype = 'Project Based Stock',fields = ['item','warehouse','project','name', 'company','batch','name']):
        if (doc.company == pbs.company) and (pbs.item == d.item_code):
            if (d.batch_no != None):    #To choose item being reconciled with a batch
                if (pbs.warehouse == d.warehouse) and (pbs.project == d.project) and (pbs.batch == d.batch_no):
                    pb = frappe.get_doc('Project Based Stock',pbs.name)
                    pb.db_set('stock', d.qty)
                    pb.db_set('stock_reconciliation', doc.name)
                    flag = 1
            else:   #To choose item being reconciled without a batch
                if (pbs.warehouse == d.warehouse) and (pbs.project == d.project):
                    pb = frappe.get_doc('Project Based Stock',pbs.name)
                    pb.db_set('stock', d.qty)
                    pb.db_set('stock_reconciliation', doc.name)
                    flag = 1
    
                    
        if flag == 1:
            break
    
    if flag == 0: # If no entries has been made for the item in the Project based Stock, new entries need to made and saved
        new_pbs = frappe.new_doc('Project Based Stock')
        new_pbs.company = doc.company
        new_pbs.item = d.item_code
        new_pbs.stock =  d.current_qty
        new_pbs.warehouse = d.warehouse
        new_pbs.batch = d.batch_no
        new_pbs.last_updated = doc.posting_date
        new_pbs.stock_reconciliation = doc.name
        new_pbs.save()