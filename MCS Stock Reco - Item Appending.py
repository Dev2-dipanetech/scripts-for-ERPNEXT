#  Doctype : MCS Stock Reconciliation : Before Save : This is to add item in the child table based on item or warehouse being picked at the top
#  The code pulls all the entries from Project Based Stock and fills the child table with matching data

if (doc.picked == 0) :  # This code works only if the 'Picked' is unchecked
    if doc.get_via == 'Item': # when reconciliation needs to be done on the basis of item
        for pbs in frappe.get_all('Project Based Stock',fields =  ['item','project','company','uom','stock','warehouse','batch']):
            if (pbs.stock == '0') or (pbs.stock =='0.0'):   # This to make sure to fetch items whose stock is not '0'
                continue
            if pbs.item == doc.item:
                doc.append('items',{
                    'item_code' : pbs.item,
                    'warehouse': pbs.warehouse,
                    'qty': pbs.stock,
                    'current_qty': pbs.stock,
                    'project': pbs.project,
                    'batch': pbs.batch
                })
        doc.picked = 1

    if doc.get_via == 'Warehouse':  # when reconciliation needs to be done on the basis of warehouse
            for pbs in frappe.get_all('Project Based Stock',fields =  ['item','project','company','uom','stock','warehouse','batch']):
                if (pbs.stock == '0') or (pbs.stock =='0.0'):   # This to make sure to fetch items whose stock is not '0'
                    continue
                if pbs.warehouse == doc.warehouse:
                    doc.append('items',{
                        'item_code' : pbs.item,
                        'warehouse': pbs.warehouse,
                        'qty': pbs.stock,
                        'current_qty': pbs.stock,
                        'project': pbs.project,
                        'batch': pbs.batch
                    })
                    doc.picked = 1