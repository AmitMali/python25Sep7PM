class Person:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def getInfo(self):
        print(f'name = {self.name}\nemail = {self.email}')



class Trainer(Person):
    def __init__(self,name,email,course):
        super().__init__(name,email)
        self.course=course
    def getInfo(self):
        print(f'name = {self.name}\nemail = {self.email}\ncourse = {self.course}')
class Student(Person):
    def __init__(self,name,email,course,fees,batch):
        super().__init__(name,email)
        self.course=course
        self.fees=fees
        self.batch=batch
    def getInfo(self):
        print(f'name = {self.name}\nemail = {self.email}\ncourse = {self.course}\nfees = {self.fees}\nbatch = {self.batch}')


amit=Trainer("amit","amit@gmail.com","python")
amit.getInfo()
print(amit.course)
john=Student("john Doe","john@gmail.com","python","5000","7pm")
john.getInfo()