import hr
import disgruntled

salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = hr.HourlyWorkedEmployee(1, 'John Doe', 40, 15)
Commission_employee = hr.CommissionEmployee(1, 'John DSouza', 1000, 250)
Disgrunted_Employee = disgruntled.disgruntledEmployee(20101, 'Anonymous')
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee, hourly_employee, Commission_employee,Disgrunted_Employee
])
"""
#employee = hr.Employee(1, 'InValid')
#payroll_system = hr.PayrollSystem()
#payroll_system.calculate_payroll([employee])

While you can instantiate an Employee object, the object can’t be used by the PayrollSystem. Why? Because it can’t 
.calculate_payroll() for an Employee. To meet the requirements of PayrollSystem, you’ll want to convert the Employee 
class, which is currently a concrete class, to an abstract class. That way, no employee is ever just an Employee, 
but one that implements .calculate_payroll(). 

Abstract Base Classes in Python:-
The Employee class in the example above is what is called an abstract base class. 
Abstract base classes exist to be inherited, but never instantiated. Python provides the abc module to define 
abstract base classes. You can use leading underscores in your class name to communicate that objects of that class 
should not be created. Underscores provide a friendly way to prevent misuse of your code, but they don’t prevent 
eager users from creating instances of that class. 

The abc module in the Python standard library provides functionality to prevent creating objects from abstract base classes.

You can modify the implementation of the Employee class to ensure that it can’t be instantiated:


#employee=hr.Employee(1,'abstract')

The output shows that the class cannot be instantiated because it contains an abstract method calculate_payroll(). 
Derived classes must override the method to allow creating objects of their type.The output shows that the class 
cannot be instantiated because it contains an abstract method calculate_payroll(). Derived classes must override the 
method to allow creating objects of their type. 
"""
