pbs = frappe.get_all('Project Based Stock', fields = ['name','project', 'company', 'item', 'stock', 'warehouse','batch'])

for i in range (len(pbs)):
    j = i+1
    a = pbs[i]
    sum_stock = a.stock
    if j == len(pbs):
        break
    for k in range (j, len(pbs)):
        b = pbs[k]
        if (a.project == b.project) and (a.company == b.company) and (a.item == b.item) and (a.warehouse == b.warehouse):
            if a.batch != b.batch:
                pass
            else:
                log(f'Check {a.name} and {b.name}')
                break