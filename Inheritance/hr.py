"""Creating Class Hierarchies
Inheritance is the mechanism you’ll use to create hierarchies of related classes. These related classes will share a common interface that will be defined in the base classes. Derived classes can specialize the interface by providing a particular implementation where applies.
In this section, you’ll start modeling an HR system. The example will demonstrate the use of inheritance and how
derived classes can provide a concrete implementation of the base class interface.

The HR system needs to process payroll for the company’s employees, but there are different types of employees
depending on how their payroll is calculated.

You start by implementing a PayrollSystem class that processes payroll:"""


class PayrollSystem:

    def calculate_payroll(self, employees):
        print('Calculating employee payroll')
        print('============================')
        for employee in employees:
            print(f'Payroll for:{employee.id}- {employee.name}')
            print(f'-Check Amount:{employee.calculate_payroll()}')
            print('')


"""The PayrollSystem implements a .calculate_payroll() method that takes a collection of employees and prints their id, name, and check amount using the .calculate_payroll() method exposed on each employee object.

Now, you implement a base class Employee that handles the common interface for every employee type:"""


class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name


"""Employee is the base class for all employee types. It is constructed with an id and a name. What you are saying is that every Employee must have an id assigned as well as a name.

The HR system requires that every Employee processed must provide a .calculate_payroll() interface that returns the weekly salary for the employee. The implementation of that interface differs depending on the type of Employee.

For example, administrative workers have a fixed salary, so every week they get paid the same amount:"""


class SalaryEmployee(Employee):

    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


"""You create a derived class SalaryEmployee that inherits Employee. The class is initialized with the id and name 
required by the base class, and you use super() to initialize the members of the base class 

SalaryEmployee also requires a weekly_salary initialization parameter that represents the amount the employee makes per week.

The class provides the required .calculate_payroll() method used by the HR system. The implementation just returns the amount stored in weekly_salary.


The company also employs manufacturing workers that are paid by the hour, so you add an HourlyEmployee to the HR system:
"""


class HourlyWorkedEmployee(Employee):

    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


"""
The HourlyEmployee class is initialized with id and name, like the base class, plus the hours_worked and the hour_rate required to calculate the payroll. The .calculate_payroll() method is implemented by returning the hours worked times the hour rate.

Finally, the company employs sales associates that are paid through a fixed salary plus a commission based on their sales, so you create a CommissionEmployee class:

"""


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


"""

You derive CommissionEmployee from SalaryEmployee because both classes have a weekly_salary to consider. At the same 
time, CommissionEmployee is initialized with a commission value that is based on the sales for the employee. 
.calculate_payroll() leverages the implementation of the base class to retrieve the fixed salary and adds the 
commission value. Since CommissionEmployee derives from SalaryEmployee, you have access to the weekly_salary property 
directly, and you could’ve implemented .calculate_payroll() using the value of that property. The problem with 
accessing the property directly is that if the implementation of SalaryEmployee.calculate_payroll() changes, 
then you’ll have to also change the implementation of CommissionEmployee.calculate_payroll(). It’s better to rely on 
the already implemented method in the base class and extend the functionality as needed. """

from abc import ABC,abstractmethod

class Employee(ABC):

    def __init__(self,id,name):

        self.id=id
        self.name=name

    @abstractmethod
    def calculate_payroll(self):
        pass

"""You derive Employee from ABC, making it an abstract base class. Then, you decorate the .calculate_payroll() method with the @abstractmethod decorator.

This change has two nice side-effects:

You’re telling users of the module that objects of type Employee can’t be created.
You’re telling other developers working on the hr module that if they derive from Employee, then they must override the .calculate_payroll() abstract method"""





