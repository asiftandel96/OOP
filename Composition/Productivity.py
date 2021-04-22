"""Composition to Model “Has A” Relationship
Composition models a has a relationship. With composition, a class Composite has an instance of class Component and can leverage its implementation. The Component class can be reused in other classes completely unrelated to the Composite.

In the composition example above, the Employee class has an Address object. Address implements all the functionality to handle addresses, and it can be reused by other classes.

Other classes like Customer or Vendor can reuse Address without being related to Employee. They can leverage the same implementation ensuring that addresses are handled consistently across the application.

A problem you may run into when using composition is that some of your classes may start growing by using multiple components. Your classes may require multiple parameters in the constructor just to pass in the components they are made of. This can make your classes hard to use.

A way to avoid the problem is by using the Factory Method to construct your objects. You did that with the composition example.

If you look at the implementation of the EmployeeDatabase class, you’ll notice that it uses ._create_employee() to construct an Employee object with the right parameters.

This design will work, but ideally, you should be able to construct an Employee object just by specifying an id, for example employee = Employee(1).

The following changes might improve your design. You can start with the productivity module:"""


class _ProductivitySystem:

    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('role_id')
        return role_type()

    def track(self, employees, hours):
        print('Track Employee Productivity')
        print('===========================')
        for employee in employees:
            employee.work(hours)
        print('')


class ManagerRole:
    def perform_duties(self, hours):
        return f'screams and yells for {hours} hours.'


class SecretaryRole:
    def perform_duties(self, hours):
        return f'does paperwork for {hours} hours.'


class SalesRole:
    def perform_duties(self, hours):
        return f'expends {hours} hours on the phone.'


class FactoryRole:
    def perform_duties(self, hours):
        return f'manufactures gadgets for {hours} hours.'


# Role Classes implementation Omitted

_productivity_system = _ProductivitySystem()


def get_role(role_id):
    return _productivity_system.get_role(role_id)


def track(employees, hours):
    _productivity_system.track(employees, hours)


"""First, you make the _ProductivitySystem class internal, and then provide a _productivity_system internal variable 
to the module. You are communicating to other developers that they should not create or use the _ProductivitySystem 
directly. Instead, you provide two functions, get_role() and track(), as the public interface to the module. This is 
what other modules should use. 

What you are saying is that the _ProductivitySystem is a Singleton, and there should only be one object created from it."""
