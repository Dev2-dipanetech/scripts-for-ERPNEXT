# Doctype : Sales Order : Before Save : To block sales order if the chosen uom is not present in the uom conversion list

count = 0
for d in (doc.get("items")):
    ch_item = (frappe.get_doc("Item", d.item_code).uoms)
    flag = 1
    
    for item in ch_item:
        uom_conv_id = (str(item)).strip("UOMConversionDetail").strip('(' + ')')
        
        if (str(d.uom)) == str(frappe.db.get_value("UOM Conversion Detail", uom_conv_id, 'uom')):
            flag = 0
            break
    
    if flag == 1:
        frappe.throw(f"Please select valid UOM for {str(d.item_code)} in row: {(count+1)}")
    
    count = count + 1