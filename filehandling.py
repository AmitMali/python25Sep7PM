# myfile=open("sample.txt")
# print(myfile.read())
# myfile.close()


# with open("sample.txt") as myfile:
#     print(myfile.readlines())

# with open("sample2.txt","a") as myfile2:
#     myfile2.write("updated data\n")


while True:
    name,email,contact=input("Name:"),input("Email:"),input("Contatct")
    with open("users.csv","a") as users:
        users.write(f"{name},{email},{contact}\n")
        confirm=input("Add more Y=yes,N=No\n")
        if confirm=='n' or confirm=='N':
            break;