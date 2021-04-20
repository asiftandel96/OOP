"""Composition in Python
Composition is an object oriented design concept that models a has a relationship. In composition, a class known as composite contains an object of another class known to as component. In other words, a composite class has a component of another class.

Composition allows composite classes to reuse the implementation of the components it contains. The composite class doesn’t inherit the component class interface, but it can leverage its implementation.

The composition relation between two classes is considered loosely coupled. That means that changes to the component class rarely affect the composite class, and changes to the composite class never affect the component class.

This provides better adaptability to change and allows applications to introduce new requirements without affecting existing code.

When looking at two competing software designs, one based on inheritance and another based on composition, the composition solution usually is the most flexible. You can now look at how composition works.

You’ve already used composition in our examples. If you look at the Employee class, you’ll see that it contains two attributes:

id to identify an employee.
name to contain the name of the employee.
These two attributes are objects that the Employee class has. Therefore, you can say that an Employee has an id and has a name.

Another attribute for an Employee might be an Address:"""


class Address:

    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.street2 = street2

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city},{self.state},{self.zipcode}')
        return '\n'.join(lines)


"""You implemented a basic address class that contains the usual components for an address. You made the street2 
attribute optional because not all addresses will have that component. """
