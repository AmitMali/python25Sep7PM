import mymodules as mm
import random as rnd
# mm.greeting()

# print(int(rnd.random()*10))
# print(int(rnd.randrange(1,7)))
cities=['nashik','pune','mumbai','nagpur','chennai','kolkata','bangalore']

print(rnd.choice(cities))

names=['amit','samrath','aadinath','aaditya','ridrani','poonam','siom','tejas','john','salman']
def makeGroup(ls):
    group1=[]
    group2=[]
    group="A"
    while len(ls)!=0:
        if group == "A":
            name = rnd.choice(ls)
            group1.append(name)
            ls.remove(name)
            group = "B"
        elif group == "B":
            name = rnd.choice(ls)
            group2.append(name)
            ls.remove(name)
            group = "A"

    print(group1)
    print(group2)

# makeGroup(names)

import math
print(math.pi)
print(math.factorial(5))
print(math.ceil(10.4))
print(math.floor(10.4))
