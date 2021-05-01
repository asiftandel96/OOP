"""-------------------Using Advanced Generator Methods------------------------  """

"""You’ve seen the most common uses and constructions of generators, but there are a few more tricks to cover. In 
addition to yield, generator objects can make use of the following methods: 

1 .send()
2 .throw()
3 .close()

"""


class Generator_Method:
    def __init__(self):
        pass

    def is_palindrome(self,num):
        # skip single_digits
        if num // 10 == 0:
            return False
        temp = num
        reversed_num = 0

        while temp != 0:
            reversed_num = (reversed_num * 10) + (temp % 10)
            temp = temp // 10

        if num == reversed_num:
            return True
        else:
            return False

    def infinte_sequence(self):
        num = 0
        while True:
            if self.is_palindrome(num):
                i = (yield num)
                if i is not None:
                    num = i
            num += 1


"""There are a lot of changes here! The first one you’ll see is in line 5, where i = (yield num). Though you learned 
earlier that yield is a statement, that isn’t quite the whole story. 

As of Python 2.5 (the same release that introduced the methods you are learning about now), yield is an expression, 
rather than a statement. Of course, you can still use it as a statement. But now, you can also use it as you see in 
the code block above, where i takes the value that is yielded. This allows you to manipulate the yielded value. More 
importantly, it allows you to .send() a value back to the generator. When execution picks up after yield, i will take 
the value that is sent. 

You’ll also check if i is not None, which could happen if next() is called on the generator object. (This can also 
happen when you iterate with a for loop.) If i has a value, then you update num with the new value. But regardless of 
whether or not i holds a value, you’ll then increment num and start the loop again. 

Now, take a look at the main function code, which sends the lowest number with another digit back to the generator. 
For example, if the palindrome is 121, then it will .send() 1000: """

if __name__ == "__main__":
    a = Generator_Method()
    pal_gen = a.infinte_sequence()
    for i in pal_gen:
        print(i)
        digits = len(str(i))
        if digits == 5:
            pal_gen.close()
            # pal_gen.throw(ValueError("We don't like large palindromes"))
        pal_gen.send(10 ** digits)
