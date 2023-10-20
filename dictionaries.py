person={
    "languages":["php","python","javascript"],
    "courses":["full stack","web development"],
    "contact":9595949452,
    "name":"Amit Mali",
    "married":True,
    "address":{
        "State":"Maharastra",
        "city":"Nashik"
    }
}

# print(person["name"])
# print(person["address"]["city"])

# for key in person:
#     print(person[key])

# for key in person.keys():
#     print(key)

# for value in person.values():
#     print(value)


# for key ,value in person.items():
#     print(key,value)

# person["name"]="Amit"

person["courses"].append("C,C++")
print(person)

no1=10
no2=10

no1=20
no2=30

print(hex(id(no1)))
print(hex(id(no2)))
