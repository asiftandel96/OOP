class Student_Raj:

    def __init__(self,ID,RollNo,FinalMarks):

        self.ID=ID
        self.RollNo=RollNo
        self.FinalMarks=FinalMarks

    def display(self):
        print('The ID =',self.ID)
        print('The RollNo=',self.RollNo)
        print('The Final Marks=',self.FinalMarks)

class Student_RajCollege(Student_Raj):

    def __init__(self,ID,RollNo,FinalMarks,Attendance):
        super().__init__(ID,RollNo,FinalMarks)
        self._Attendance=Attendance

    def display(self):
        print('The Attendance=',self.Attendance)

class Student_RajATT(Student_RajCollege):

    def __init__(self,ID,RollNo,FinalMarks,Attendance,PersonalDetails):
        super().__init__(ID,RollNo,FinalMarks,Attendance)
        self.__PersonalDetails=PersonalDetails
Student1=Student_RajATT(1,1234,89,77,'Whatthe')
print(dir(Student1))
print(Student1._Attendance) # Protected can be access from sub-class only
print(Student1.FinalMarks) # Public can be access from anywhere
#print(Student1.__PersonalDetails) # Private can't be accessed
