from Employee import TemporarySecretary

print(TemporarySecretary.__mro__)  # MRO(Method Resolution Order)
import hr
import Employee
import Productivity

Manager = Employee.Manager(1, 'Mary Poppins', 1000)
Secretary = Employee.Secretary(2, 'John Scoe', 1000)
SalesPerson = Employee.SalesPerson(3, 'Adil ', 2000, 250)
FactoryWorker = Employee.FactoryWorker(4, 'Adis', 40, 15)
Temporary_Secretary = Employee.TemporarySecretary(5, 'Adarsh', 40, 9)
employees = ([Manager, Secretary, SalesPerson, FactoryWorker,Temporary_Secretary])
Productivity_System = Productivity.ProductivitySystem()
Productivity_System.track(employees, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)
