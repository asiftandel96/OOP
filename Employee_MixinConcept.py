"""Mixing Features With Mixin Classes One of the uses of multiple inheritance in Python is to extend a class features
through mixins. A mixin is a class that provides methods to other classes but are not considered a base class.

A mixin allows other classes to reuse its interface and implementation without becoming a super class. They implement
a unique behavior that can be aggregated to other unrelated classes. They are similar to composition but they create
a stronger relationship.

Let’s say you want to convert objects of certain types in your application to a dictionary representation of the
object. You could provide a .to_dict() method in every class that you want to support this feature,
but the implementation of .to_dict() seems to be very similar.

This could be a good candidate for a mixin. You start by slightly modifying the Employee class from the composition example:


"""

from Representation_Mixin import AsDictionaryMixin


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
        print(f'-{duties}')
        print(' ')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()


"""The change is very small. You just changed the role and payroll attributes to be internal by adding a leading 
underscore to their name. You will see soon why you are making that change. """

"""All you have to do is inherit the AsDictionaryMixin to support the functionality. It will be nice to support the 
same functionality in the Address class, so the Employee.address attribute is represented in the same way: """
