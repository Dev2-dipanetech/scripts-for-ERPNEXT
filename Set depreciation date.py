if doc.available_for_use_date:
    date = frappe.utils.getdate(doc.available_for_use_date)
    if date.month in [1,3,5,7,9,10,12]:
        if date.day < 31:
            new_date = date.replace(day = 31)
        else:
            new_date = frappe.utils.add_months(date, 1)
 
    
    if date.month in [4,6,8, 11]:
        if date.day < 30:
            new_date = date.replace(day = 30)
        else:
            new_date = frappe.utils.add_months(date, 1)
 
    
    if date.month == 2:
        if (date.year % 4) == 0:
            last_day = 29
        else:
            last_day = 28
            
        if date.day < last_day:
            new_date = date.replace(day = last_day)
        else:
            new_date = frappe.utils.add_months(date, 1)
            new_date = new_date.replace(day = 31)


for d in doc.finance_books:
    d.depreciation_start_date = new_date
 
