def headline(text: str, centered: bool = False) -> str:
    if not centered:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


print(headline("python type checking"))
print(headline("use mypy", centered=True))

"""This is essentially the same code you saw earlier: the definition of headline() and two examples that are using 
it. """


"""Pros and Cons The previous section gave you a little taste of what type checking in Python looks like. You also 
saw an example of one of the advantages of adding types to your code: type hints help catch certain errors. Other 
advantages include: 

Type hints help document your code. Traditionally, you would use docstrings if you wanted to document the expected 
types of a function’s arguments. This works, but as there is no standard for docstrings (despite PEP 257 they can’t 
be easily used for automatic checks. 

Type hints improve IDEs and linters. They make it much easier to statically reason about your code. This in turn 
allows IDEs to offer better code completion and similar features. With the type annotation, PyCharm knows that text 
is a string, and can give specific suggestions based on this: 

Code completion in PyCharm on a typed variable Type hints help you build and maintain a cleaner architecture. The act 
of writing type hints forces you to think about the types in your program. While the dynamic nature of Python is one 
of its great assets, being conscious about relying on duck typing, overloaded methods, or multiple return types is a 
good thing. 

Of course, static type checking is not all peaches and cream. There are also some downsides you should consider:

Type hints take developer time and effort to add. Even though it probably pays off in spending less time debugging, 
you will spend more time entering code. 

Type hints work best in modern Pythons. Annotations were introduced in Python 3.0, and it’s possible to use type 
comments in Python 2.7. Still, improvements like variable annotations and postponed evaluation of type hints mean 
that you’ll have a better experience doing type checks using Python 3.6 or even Python 3.7. 

Type hints introduce a slight penalty in start-up time. If you need to use the typing module the import time may be significant, especially in short scripts."""