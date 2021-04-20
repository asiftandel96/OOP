import hr_revamped
import Employee_revamped
import Productivity_revamped
import contact

Manager = Employee_revamped.Manager(1, 'Mary Poppins', 1000)
Manager.address = contact.Address(
    '121 Admin Rd',
    'Concord',
    'NH',
    '03301'
)
Secretary = Employee_revamped.Secretary(2, 'John Scoe', 1000)
Secretary.address = contact.Address(
    '67 Paperwork Ave.',
    'Manchester',
    'NH',
    '03101'
)
SalesPerson = Employee_revamped.SalesPerson(3, 'Adil ', 2000, 250)
SalesPerson.address = contact.Address(
    '68 Paperwork Ave.',
    'Manchester',
    'NH',
    '03102'
)
FactoryWorker = Employee_revamped.FactoryWorker(4, 'Adis', 40, 15)
FactoryWorker.address = contact.Address(
    '69 Paperwork Ave.',
    'Manchester',
    'NH',
    '03103'
)
Temporary_Secretary = Employee_revamped.TemporarySecretary(5, 'Adarsh', 40, 9)
Temporary_Secretary.address = contact.Address(
    '70 Paperwork Ave.',
    'London',
    'NH',
    '04104'
)
employees = ([Manager, Secretary, SalesPerson, FactoryWorker, Temporary_Secretary])
Productivity_System = Productivity_revamped.ProductivitySystem()
Productivity_System.track(employees, 40)
payroll_system = hr_revamped.PayrollSystem()
payroll_system.calculate_payroll(employees)
