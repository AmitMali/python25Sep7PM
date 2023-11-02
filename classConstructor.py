class Person:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def getInfo(self):
        print(f'name = {self.name}\nemail = {self.email}')

amit=Person("amit mali","amit@gmail.com")
amit.getInfo()
john=Person("John Doe","john@google.com")
john.getInfo()