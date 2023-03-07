#Doctype : Delivery Note : Before Save : This code blocks entries bieng drafted if the stock quantity exceeds the amount present in the warehouse
# This is bieng validated through Project Based Stock
# MAY REQUIRE UPDATE FOR BATCHES, NEED TO CONFIRM


if (doc.company == "Multicolor Steels (India) Pvt Ltd"):
    # pbs = frappe.db.get_all('Project Based Stock', fields = ['item','warehouse','project','stock'])
    
    for d in doc.get("items"):
            warehouse = d.warehouse
            item_code = d.item_code
            quantity = d.stock_qty
            if doc.project:
                project = doc.project
            else:
                project = d.project
            
            flag = 0
            
            docu = frappe.get_doc('Item',d.item_code)
            if (docu.is_stock_item) == 0:
                pass
            else:
            
                pbs = frappe.db.get_all('Project Based Stock', fields = ['item','warehouse','project','stock'])
                for p in pbs:
                    if (warehouse == p.warehouse) and (item_code == p.item) and (project == p.project):
                        flag = 1
                        # frappe.throw(warehouse)
                        if (str((float(quantity)) > (float(p.stock))))=='True':
                            frappe.throw(f"Stock requirement exceeds for Item: {item_code} for Project: {project} in {warehouse} warehouse")
                            # frappe.throw(f"Quantity exceeds for the Stock present in the {warehouse} warehouse for item : {item_code} for project : {project}")
                        break
                if flag == 0:
                    # frappe.throw("check")
                    frappe.throw(f"Item : {item_code} not present in the selected warehouse (Warehouse Name: {warehouse})  for Project: {project}")