"""Polymorphism with a Function and objects:
It is also possible to create a function that can take any object, allowing for polymorphism.
In this example, let’s create a function called “func()” which will take an object which we will name “obj”.
Though we are using the name ‘obj’, any instantiated object will be able to be called into this function.
Next, lets give the function something to do that uses the ‘obj’ object we passed to it.
In this case lets call the three methods, viz., capital(), language() and type(), each of which is defined in the two classes
‘India’ and ‘USA’.With those, we can call their action using the same func() function:"""


class India:

    def capital(self):
        print('Delhi is the capital of India')

    def language(self):
        print('Hindi is the most spoken language in India')

    def type(self):
        print('India is a developing country')


class Sweden:

    def capital(self):
        print('Stockholm is the capital of Sweden')

    def language(self):
        print('Swedish is the most spoken language in Sweden')

    def type(self):
        print('Sweden is a developed country')


def func(obj):
    print()
    obj.capital()
    obj.language()
    obj.type()
    print()


obj_ind = India()
obj_sweden = Sweden()

func(obj_ind)
func(obj_sweden)
