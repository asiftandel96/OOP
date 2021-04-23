def len(obj):
    return obj.__len__()


print(len('str'))

"""len() can return the length of any object that has implemented the .__len__() method. How can we add type hints to 
len(), and in particular the obj argument? 

The answer hides behind the academic sounding term structural subtyping. One way to categorize type systems is by 
whether they are nominal or structural: 

In a nominal system, comparisons between types are based on names and declarations. The Python type system is mostly 
nominal, where an int can be used in place of a float because of their subtype relationship. 

In a structural system, comparisons between types are based on structure. You could define a structural type Sized 
that includes all instances that define .__len__(), irrespective of their nominal type. 


There is ongoing work to bring a full-fledged structural type system to Python through PEP 544 which aims at adding a 
concept called protocols. Most of PEP 544 is already implemented in Mypy though. 

A protocol specifies one or more methods that must be implemented. For example, all classes defining .__len__() 
fulfill the typing.Sized protocol. We can therefore annotate len() as follows: 


There is ongoing work to bring a full-fledged structural type system to Python through PEP 544 which aims at adding a 
concept called protocols. Most of PEP 544 is already implemented in Mypy though. 

A protocol specifies one or more methods that must be implemented. For example, all classes defining .__len__() 
fulfill the typing.Sized protocol. We can therefore annotate len() as follows: 

"""

from typing import Sized


def len_1(obj: Sized) -> int:
    return obj.__len__()


print(len_1('Str'))

"""Other examples of protocols defined in the typing module include Container, Iterable, Awaitable, and ContextManager.

You can also define your own protocols. This is done by inheriting from Protocol and defining the function signatures 
(with empty function bodies) that the protocol expects. The following example shows how len() and Sized could have 
been implemented: """

from typing_extensions import Protocol


class Sized(Protocol):
    def __len__(self) -> int:
        return self.__len__()


def __len__(obj: Sized) -> int:
    return obj.__len__()
