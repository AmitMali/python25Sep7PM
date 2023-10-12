foo="Anappleadaykeepsdoctoraway"
# print(len(foo))
print(foo[3:8])
print(foo[0:20:2])
print(foo[-1])
print(foo[::-1])

def isPalindrom(str):
    return True if str==str[::-1] else False

# print(isPalindrom("racecar"))
# print(isPalindrom("amit"))

print(foo.upper())
print(foo.lower())
print(foo.title())
print(foo.isalpha())
print(foo.isnumeric())

filename="somedoc.pdf"
print(filename.endswith(".pdf"))
cities="nashik mumbai calcata delhi pune"
print(cities.split(" "))
cites2=['nashik', 'mumbai', 'calcata', 'delhi', 'pune']
print(",".join(cites2))

# print(type(foo))
print("foo".rjust(20))
print("Login".center(30,"="))
print("         amit mali     ".strip())
print(r"first line\nsecond line")

