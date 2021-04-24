"""Returning self or cls As noted, you should typically not annotate the self or cls arguments. Partly, this is not
necessary as self points to an instance of the class, so it will have the type of the class. In the Card example,
self has the implicit type Card. Also, adding this type explicitly would be cumbersome since the class is not defined
yet. You would have to use the string literal syntax, self: "Card".

There is one case where you might want to annotate self or cls, though. Consider what happens if you have a superclass
that other classes inherit from, and which has methods that return self or cls:"""
from datetime import date
from typing import TypeVar, Type

#TAnimal is the subclasses of Animal that why it is defined here
TAnimal = TypeVar("TAnimal", bound="Animal")


class Animal:

    def __init__(self, name: str, birthday: date) -> None:
        self.name = name
        self.birthday = birthday

    @classmethod
    def newborn(cls: Type[TAnimal], name: str) -> TAnimal:
        return cls(name, date.today())

    def twin(self: TAnimal, name: str) -> TAnimal:
        cls = self.__class__

        return cls(name, self.birthday)


class Dog(Animal):
    def bark(self) -> None:
        print(f"{self.name} says woof!")


fido = Dog.newborn("Fido")
pluto = fido.twin("Pluto")
fido.bark()
pluto.bark()

"""The issue is that even though the inherited Dog.newborn() and Dog.twin() methods will return a Dog the annotation 
says that they return an Animal. 

In cases like this you want to be more careful to make sure the annotation is correct. The return type should match 
the type of self or the instance type of cls. This can be done using type variables that keep track of what is 
actually passed to self and cls: """

"""There are a few things to note in this example:

The type variable TAnimal is used to denote that return values might be instances of subclasses of Animal.

We specify that Animal is an upper bound for TAnimal. Specifying bound means that TAnimal will only be Animal or one 
of its subclasses. This is needed to properly restrict the types that are allowed. 

The typing.Type[] construct is the typing equivalent of type(). You need it to note that the class method expects a class
 and returns an instance of that class."""

