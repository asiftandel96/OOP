import json
from Payroll import calculate_payroll, LTDPolicy
from Productivity import track
from Employee import Employee, employee_database


def print_dict(d):
    print(json.dumps(d, indent=2))


employees = employee_database.employees

# temp_secretary = Employee(5)
sales_employees = employees[2]
ltd_policy = LTDPolicy()
sales_employees.apply_payroll_policy(ltd_policy)

track(employees, 40)
calculate_payroll(employees)

# print('temp secretary:')
# print(temp_secretary.to_dict())

"""The program works the same as before, but now you can see that a single Employee object can be created from its id and display its dictionary representation.

The Employee class is a composite that contains multiple objects providing different functionality. It contains an Address that implements all the functionality related to where the employee lives.

Employee also contains a productivity role provided by the productivity module, and a payroll policy provided by the hr module. These two objects provide implementations that are leveraged by the Employee class to track work in the .work() method and to calculate the payroll in the .calculate_payroll() method.

You are using composition in two different ways. The Address class provides additional data to Employee where the role and payroll objects provide additional behavior.

Still, the relationship between Employee and those objects is loosely coupled, which provides some interesting capabilities that you’ll see in the next section.

"""
