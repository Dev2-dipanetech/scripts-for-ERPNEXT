# Doctype : MCS Stock Reconciliation : After Save : This is to feed Difference Quantity with the difference between Current quantity
#  and new quantity


if doc.get("items"):
    for d in doc.get("items"):
        d.diff_qty = float(d.qty) - float(d.current_qty)