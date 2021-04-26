class Bank:

    def __init__(self):
        self.Bank_details = 'ABC Bank'
        self.Bank_Branch = 'Washington DC'
        print(f"The Bank Details is {self.Bank_details}")
        print(f"The Bank Details is {self.Bank_Branch}")


class Customer_Details:

    def __init__(self):
        Bank.__init__(self)
        self._Customer_Id = '1222222222'
        self._Account_Number = '1222222222222222222222'
        self._Debit_Card_Details = '111111111112222222222'
        self.__Password = '99999999999'
        print(f"The Customer_Id is {self._Customer_Id}")
        print(f"The Account_Number is {self._Account_Number}")
        print(f"The Debit Card Details is {self._Debit_Card_Details}")
        #print(f"The Password is {self.__Password}")


obj1 = Customer_Details()
obj2 = Bank()
obj2.Bank_details
obj2.Bank_Branch
obj1._Customer_Id
obj1._Account_Number
obj1._Debit_Card_Details
#obj1.__Password
