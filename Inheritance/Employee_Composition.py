"""You can start by implementing an EmployeeDatabase class:"""
from Productivity_Composition import ProductivitySystem
from hr_Composition import PayrollSystem
from Contacts_Composition import AddressBook
from Representation_Mixin import AsDictionaryMixin


class EmployeeDatabase:

    def __init__(self):
        self._employees = [
            {
                'id': 1,
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            {
                'id': 2,
                'name': 'John Smith',
                'role': 'secretary'
            },
            {
                'id': 3,
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
            {
                'id': 4,
                'name': 'Jane Doe',
                'role': 'factory'
            },
            {
                'id': 5,
                'name': 'Robin Williams',
                'role': 'secretary'
            },
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook()

    @property
    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)


"""The EmployeeDatabase keeps track of all the employees in the company. For each employee, it tracks the id, name, 
and role. It has an instance of the ProductivitySystem, the PayrollSystem, and the AddressBook. These instances are 
used to create employees. 

It exposes an .employees property that returns the list of employees. The Employee objects are created in an internal method ._create_employee(). Notice that you don’t have different types of Employee classes. You just need to implement a single Employee class:


"""


class Employee(AsDictionaryMixin):

    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self._role = role
        self._payroll = payroll

    def work(self, hours):
        duties = self._role.perform_duties(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self._payroll.track_hours(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()


"""The Employee class is initialized with the id, name, and address attributes. It also requires the productivity 
role for the employee and the payroll policy. 

The class exposes a .work() method that takes the hours worked. This method first retrieves the duties from the role. In other words, it delegates to the role object to perform its duties.

In the same way, it delegates to the payroll object to track the work hours. The payroll, as you saw, uses those hours to calculate the payroll if needed."""
