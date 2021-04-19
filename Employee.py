"""The Class Explosion Problem If you are not careful, inheritance can lead you to a huge hierarchical structure of
classes that is hard to understand and maintain. This is known as the class explosion problem.

You started building a class hierarchy of Employee types used by the PayrollSystem to calculate payroll. Now,
you need to add some functionality to those classes, so they can be used with the new ProductivitySystem.

The ProductivitySystem tracks productivity based on employee roles. There are different employee roles:
1.Managers: They walk around yelling at people telling them what to do. They are salaried employees and make more money.

2.Secretaries: They do all the paper work for managers and ensure that everything gets billed and payed on time.
They are also salaried employees but make less money.

3.Sales employees: They make a lot of phone calls to sell products. They have a salary, but they also get commissions
for sales.

Factory workers: They manufacture the products for the company. They are paid by the hour.

With everything in place, you start adding the new classes:
"""


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class Manager(SalaryEmployee):

    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours')


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')


class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')


class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')


"""First, you add a Manager class that derives from SalaryEmployee. The class exposes a method work() that will be used 
by the productivity system. The method takes the hours the employee worked.

Then you add Secretary, SalesPerson, and FactoryWorker and then 
implement the work() interface, so they can be used by the productivity system."""


class TemporarySecretary(Secretary, HourlyEmployee):

    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)


"""Inheriting Multiple Classes Python is one of the few modern programming languages that supports multiple 
inheritance. Multiple inheritance is the ability to derive a class from multiple base classes at the same time. 

Multiple inheritance has a bad reputation to the extent that most modern programming languages don’t support it. 
Instead, modern programming languages support the concept of interfaces. In those languages, you inherit from a 
single base class and then implement multiple interfaces, so your class can be re-used in different situations. 

This approach puts some constraints in your designs. You can only inherit the implementation of one class by directly 
deriving from it. You can implement multiple interfaces, but you can’t inherit the implementation of multiple classes. 

This constraint is good for software design because it forces you to design your classes with fewer dependencies on 
each other. You will see later in this article that you can leverage multiple implementations through composition, 
which makes software more flexible. This section, however, is about multiple inheritance, so let’s take a look at how 
it works. 

It turns out that sometimes temporary secretaries are hired when there is too much paperwork to do. The 
TemporarySecretary class performs the role of a Secretary in the context of the ProductivitySystem, but for payroll 
purposes, it is an HourlyEmployee. 

You look at your class design. It has grown a little bit, but you can still understand how it works. It seems you 
have two options: 

Derive from Secretary: You can derive from Secretary to inherit the .work() method for the role, and then override 
the .calculate_payroll() method to implement it as an HourlyEmployee. 

Derive from HourlyEmployee: You can derive from HourlyEmployee to inherit the .calculate_payroll() method, 
and then override the .work() method to implement it as a Secretary. """
