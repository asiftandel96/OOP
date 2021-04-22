"""Flexible Designs With Composition Composition is more flexible than inheritance because it models a loosely
coupled relationship. Changes to a component class have minimal or no effects on the composite class. Designs based
on composition are more suitable to change.

You change behavior by providing new components that implement those behaviors instead of adding new classes to your hierarchy.

Take a look at the multiple inheritance example above. Imagine how new payroll policies will affect the design. Try to picture what the class hierarchy will look like if new roles are needed. As you saw before, relying too heavily on inheritance can lead to class explosion.

The biggest problem is not so much the number of classes in your design, but how tightly coupled the relationships between those classes are. Tightly coupled classes affect each other when changes are introduced.

In this section, you are going to use composition to implement a better design that still fits the requirements of the PayrollSystem and the ProductivitySystem.

You can start by implementing the functionality of the ProductivitySystem:

"""


class ProductivitySystem:
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
        print(' ')


"""The ProductivitySystem class defines some roles using a string identifier mapped to a role class that implements the role. It exposes a .get_role() method that, given a role identifier, returns the role type object. If the role is not found, then a ValueError exception is raised.

It also exposes the previous functionality in the .track() method, where given a list of employees it tracks the productivity of those employees.

You can now implement the different role classes:

"""


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


"""Each of the roles you implemented expose a .perform_duties() that takes the number of hours worked. The methods return a string representing the duties.

The role classes are independent of each other, but they expose the same interface, so they are interchangeable. You’ll see later how they are used in the application."""
