stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(price+(0.1*price))


work_hours = [('abby', 100),('billy',400),('cassie',800)]


#tuple with function
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return employee_of_month,current_max

result = employee_check(work_hours)
print(result)
name,hours = employee_check(work_hours)
print(name)
print(hours)