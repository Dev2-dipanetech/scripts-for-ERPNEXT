for pbs in frappe.get_all('Project Based Stock', fields = ['name', 'stock_reconciliation'] ):
    if (pbs.stock_reconciliation == '') or (pbs.stock_reconciliation == None):
        continue
    else:
        frappe.db.set_value('Project Based Stock', pbs.name, 'p_st_reco',pbs.stock_reconciliation)