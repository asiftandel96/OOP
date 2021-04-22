"""USING THE CONCEPTS OF MULTIPLE INHERITANCE"""


class A:
    def method1(self):
        print('A class is called!!!')


class B:
    def method1(self):
        print('B is just called!!!')


class C:
    def method1(self):
        print('C is just called!!!')


class D(B, C):
    def method1(self):
        print('D is just called!!!!')
        B.method1(self)
        C.method1(self)
        A.method1(self)


d = D()
print("-----MULTIPLE INHERITANCE ")
d.method1()
# B.method1(d)
# A.method1(d)
