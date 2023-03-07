# Doctype : Stock Entry  : Before Save : This code blocks entries bieng drafted if the stock quantity exceeds the amount present in the warehouse
# This is bieng validated through Project Based Stock

# Line - 2 : To makew sure this code runs only when the company chosen is "Multicolor Steels (India) Pvt Ltd"
if doc.company == "Multicolor Steels (India) Pvt Ltd":
    pbs = frappe.db.get_all('Project Based Stock', fields = ['item','warehouse','project','stock','batch'])
    
    for d in doc.get("items"):
        warehouse = d.s_warehouse
        if (warehouse) == None: # This to make sure stock entry with new item bieng added does not get blocked by this code
            break
        t_warehouse = d.t_warehouse
        item_code = d.item_code
        quantity = d.transfer_qty
        project = d.project
        if d.batch_no:
            batch = d.batch_no

        flag = 0
        for p in pbs:
            # if warehouse == '':
            #     flag = 1
            #     break
            if d.batch_no != None:  #To choose Items with batch number
                if (warehouse == p.warehouse) and (item_code == p.item) and (project == p.project) and (batch == p.batch):
                    flag = 1
                    if (str((float(quantity)) > (float(p.stock))))=='True':
                        frappe.throw(f"Quantity exceeds for the amount present in the {warehouse} for item : {item_code} for project : {project} for batch : {batch} ")

            else:   #To choose Items without batch number
                if (warehouse == p.warehouse) and (item_code == p.item) and (project == p.project):
                    flag = 1
                    if (str((float(quantity)) > (float(p.stock))))=='True':
                        frappe.throw(f"Quantity exceeds for the amount present in the {warehouse} for item : {item_code} for project : {project}")
            
            if flag == 1:
                break
                
        
        if flag == 0:
            frappe.throw(f"Item : {item_code} not present in the selected warehouse (Warehouse Name: {warehouse})for {project} project")