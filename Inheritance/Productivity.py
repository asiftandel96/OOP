class ProductivitySystem:

    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')


"""The class tracks employees in the track() method that takes a list of employees and the number of hours to track. 
You can now add the productivity system to your program"""

"""The diagram shows the diamond problem with the current class design. TemporarySecretary uses multiple inheritance 
to derive from two classes that ultimately also derive from Employee. This causes two paths to reach the Employee 
base class, which is something you want to avoid in your designs. 

The diamond problem appears when you’re using multiple inheritance and deriving from two classes that have a common 
base class. This can cause the wrong version of a method to be called. 

As you’ve seen, Python provides a way to force the right method to be invoked, and analyzing the MRO can help you 
understand the problem. 

Still, when you run into the diamond problem, it’s better to re-think the design. You will now make some changes to leverage multiple inheritance, avoiding the diamond problem.

The Employee derived classes are used by two different systems:

The productivity system that tracks employee productivity.

The payroll system that calculates the employee payroll.

This means that everything related to productivity should be together in one module and everything related to payroll 
should be together in another. You can start making changes to the productivity module: """
