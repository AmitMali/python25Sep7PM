# print(list(range(10)))
# print(list(range(5,20)))
# print(list(range(5,20,4)))

# no=1
# while(no<=10):
#     print(no)
#     no=no+1

# def printNoTable(tableOf):
#     no=1
#     while(no<=10):
#         print(no*tableOf)
#         no=no+1

# printNoTable(2)
# printNoTable(17)

# for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     print(n)

# for n in range(1,11):
#     print(n*2)

names=['amit','rahul','sumit','pritam']

for name in names:
    print(name.upper())

for s in "this is some string":
    print(s,end=",")

print()
x=0
str="this is some string"
while (x<len(str)):
    print(str[x], end=",")
    x=x+1