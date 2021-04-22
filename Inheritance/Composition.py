from contact import Address

Address_1 = Address('55 Main St.', 'Concord', 'NH', '03301')
print(Address_1)

"""When you print() the address variable, the special method __str__() is invoked. Since you overloaded the method to 
return a string formatted as an address, you get a nice, readable representation. Operator and Function Overloading 
in Custom Python Classes gives a good overview of the special methods available in classes that can be implemented to 
customize the behavior of your objects. """

