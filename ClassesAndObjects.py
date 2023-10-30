class Human:
    def setName(self,name):
        self.name=name
    def talk(self):
        print("talking")
    def walk(self):
        print("Walking")
    def printself(self):
        print(self)

amit=Human()

amit.talk()
amit.walk()


rahul=Human()
rahul.walk()
amit.setName("amit")
rahul.setName("rahul")
print(amit.name)
print(rahul.name)
amit.printself()
rahul.printself()
