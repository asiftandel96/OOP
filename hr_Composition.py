class PayrollSystem:

    def __init__(self):
        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(3000),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }

    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            return ValueError(employee_id)
        return policy

    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print()
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')

            if employee.address:
                print('- Sent to:')
                print(employee.address)
            print('')


"""The PayrollSystem keeps an internal database of payroll policies for each employee. It exposes a .get_policy() 
that, given an employee id, returns its payroll policy. If a specified id doesn’t exist in the system, 
then the method raises a ValueError exception. 

The implementation of .calculate_payroll() works the same as before. It takes a list of employees, calculates the 
payroll, and prints the results. 

You can now implement the payroll policy classes:"""


class PayrollPolicy:

    def __init__(self):
        self.hour_worked = 0

    def track_hours(self, hours):
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


"""You first implement a PayrollPolicy class that serves as a base class for all the payroll policies. This class 
tracks the hours_worked, which is common to all payroll policies. 

The other policy classes derive from PayrollPolicy. We use inheritance here because we want to leverage the 
implementation of PayrollPolicy. Also, SalaryPolicy, HourlyPolicy, and CommissionPolicy are a PayrollPolicy. 

SalaryPolicy is initialized with a weekly_salary value that is then used in .calculate_payroll(). HourlyPolicy is 
initialized with the hour_rate, and implements .calculate_payroll() by leveraging the base class hours_worked. 

The CommissionPolicy class derives from SalaryPolicy because it wants to inherit its implementation. It is 
initialized with the weekly_salary parameters, but it also requires a commission_per_sale parameter. 

The commission_per_sale is used to calculate the .commission, which is implemented as a property so it gets 
calculated when requested. In the example, we are assuming that a sale happens every 5 hours worked, 
and the .commission is the number of sales times the commission_per_sale value. 

CommissionPolicy implements the .calculate_payroll() method by first leveraging the implementation in SalaryPolicy 
and then adding the calculated commission. 

You can now add an AddressBook class to manage employee addresses:"""
