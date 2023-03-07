#  Doctype : Sales Order : Before Submit : This code is to make sure the Sales order , if linked with blanket order, is blocked
#  if it exceeds the quantity mentioned in the blanket order. Also if the entry passes, it make updates the 
# quantity and/or amount on the blanket order

if doc.blanket_order:
    docu = frappe.get_doc('Blanket Order',doc.blanket_order)
    if docu.order_limit == 'Ceiling Amount':
        sum_amount = 0
        child_sum_amount = 0
       
        ch_items = (frappe.get_doc('Blanket Order',doc.blanket_order).items)
        for d in doc.get("items"):
            sum_amount = sum_amount + d.amount
        # frappe.throw(str(sum_amount))
        ch_items = (frappe.get_doc('Blanket Order',doc.blanket_order).items)
        for item in ch_items:
            child_sum_amount = child_sum_amount + item.ordered_amount
        if (int(sum_amount) + int(child_sum_amount))  > (int(docu.ceiling_amount)):
            frappe.throw("Order Value exceeds Ceiling Amount")
        else :
            for d in doc.get("items"):
                value = d.base_amount
                quantity = int(d.qty)
                ch_items = (frappe.get_doc('Blanket Order',doc.blanket_order).items)
                for item in ch_items:
                    if d.item_code == item.item_code:
                        if item.ordered_amount != None:
                            new_value = int(item.ordered_amount) + int(value)
                            item.db_set('ordered_amount', int(new_value))
                        else:
                            item.db_set('ordered_amount',int(value))
    
    
    if docu.order_limit == 'Item Quantity':
        for d in doc.get("items"):
            ch_items = (frappe.get_doc('Blanket Order',doc.blanket_order).items)
            for item in ch_items:
                if d.item_code == item.item_code:
                    if (int(item.ordered_qty) + int(d.qty)) > (int(item.qty)):
                        frappe.throw(f"{d.item_code} exceeds the Ordered Quantity on the blanket order: {doc.blanket_order}")