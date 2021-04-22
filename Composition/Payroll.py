class _PayrollSystem:

    def __init__(self):
        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 10),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }

    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            raise ValueError(employee_id)
        return policy

    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            if employee.address:
                print('- Sent to:')
                print(employee.address)
            print('')


class PayrollPolicy:

    def __init__(self):
        self.hour_worked = 0

    def track_work(self, hours):
        self.hour_worked += hours


class SalaryPolicy(PayrollPolicy):

    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):

    def __init__(self, hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hour_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):

    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    @property
    def commission(self):
        sales = self.hour_worked / 5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


# Policy Classes Omitted

_payrollsystem = _PayrollSystem()


def get_policy(employee_id):
    return _payrollsystem.get_policy(employee_id)


def calculate_payroll(employees):
    return _payrollsystem.calculate_payroll(employees)


"""Again, you make the _PayrollSystem internal and provide a public interface to it. The application will use the public interface to get policies and calculate payroll."""

"""Composition to Change Run-Time Behavior
Inheritance, as opposed to composition, is a tightly couple relationship. With inheritance, there is only one way to change and customize behavior. Method overriding is the only way to customize the behavior of a base class. This creates rigid designs that are difficult to change.

Composition, on the other hand, provides a loosely coupled relationship that enables flexible designs and can be used to change behavior at run-time.

Imagine you need to support a long-term disability (LTD) policy when calculating payroll. The policy states that an employee on LTD should be paid 60% of their weekly salary assuming 40 hours of work.

With an inheritance design, this can be a very difficult requirement to support. Adding it to the composition example is a lot easier. Let’s start by adding the policy class:"""


class LTDPolicy:

    def __init__(self):
        self._base_policy = None

    def track_work(self, hours):
        self._check_base_policy()
        return self._base_policy.track_work(hours)

    def calculate_payroll(self):
        self._check_base_policy()
        return self._base_policy.calculate_payroll()
        return base_salary * 0.6

    def apply_to_policy(self, base_policy):
        self._base_policy = base_policy

    def _check_base_policy(self):
        if not self._base_policy:
            raise RuntimeError('Policy Missing')


"""Notice that LTDPolicy doesn’t inherit PayrollPolicy, but implements the same interface. This is because the 
implementation is completely different, so we don’t want to inherit any of the PayrollPolicy implementation. 

The LTDPolicy initializes _base_policy to None, and provides an internal ._check_base_policy() method that raises an exception if the ._base_policy has not been applied. Then, it provides a .apply_to_policy() method to assign the _base_policy.

The public interface first checks that the _base_policy has been applied, and then implements the functionality in terms of that base policy. The .track_work() method just delegates to the base policy, and .calculate_payroll() uses it to calculate the base_salary and then return the 60%."""
