# Doctype : Sales Order : Before Cancel : This updates(as in reduces the blanket order qauntity/amount) if the order with the blanket
# order is cancelled

if doc.blanket_order:
    # frappe.throw("HALT")
    docu =  frappe.get_doc('Blanket Order',doc.blanket_order)
    for d in doc.get("items"):
        ch_items = (frappe.get_doc('Blanket Order',doc.blanket_order).items)
        for item in ch_items:
            if item.item_code == d.item_code:
                value = item.ordered_amount - d.amount
                item.db_set('ordered_amount',value)