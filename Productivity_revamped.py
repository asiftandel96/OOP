class ProductivitySystem:

    def track(self, employees, hours):
        print('Track Employee Productivity')
        print('===========================')
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name}: {result}')
        print('')


class ManagerRole:

    def work(self, hours):
        return f'screams and yells for {hours} hours .'


class SecretaryRole:

    def work(self, hours):
        return f'expend {hours} for doing some paperwork'


class SalesRole:

    def work(self, hours):
        return f'expends {hours} hours on the phone'


class FactoryWorkerRole:

    def work(self, hours):
        return f'manufactures gadget for {hours} hours'


"""The productivity module implements the ProductivitySystem class, as well as the related roles it supports. The 
classes implement the work() interface required by the system, but they don’t derived from Employee. """
