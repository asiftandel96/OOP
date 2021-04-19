import hr_revamped
import Employee_revamped
import Productivity_revamped

Manager = Employee_revamped.Manager(1, 'Mary Poppins', 1000)
Secretary = Employee_revamped.Secretary(2, 'John Scoe', 1000)
SalesPerson = Employee_revamped.SalesPerson(3, 'Adil ', 2000, 250)
FactoryWorker = Employee_revamped.FactoryWorker(4, 'Adis', 40, 15)
Temporary_Secretary = Employee_revamped.TemporarySecretary(5, 'Adarsh', 40, 9)
employees = ([Manager, Secretary, SalesPerson, FactoryWorker, Temporary_Secretary])
Productivity_System = Productivity_revamped.ProductivitySystem()
Productivity_System.track(employees, 40)
payroll_system = hr_revamped.PayrollSystem()
payroll_system.calculate_payroll(employees)

