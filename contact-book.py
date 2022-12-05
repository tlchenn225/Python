# Contact List
nameList = []
phoneList = []
num = 3

for x in range(num):
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    nameList.append(name)
    phoneList.append(phone)

print("\nName\t\tPhone")

for x in range(num):
    print("{}\t\t{}".format(nameList[x], phoneList[x]))
search_keyword = input("\nEnter name for contact: ")

print("Search result: ")

if search_keyword in nameList:
    index = nameList.index(search_keyword)
    phone = phoneList[index]
    print("Name: {},Phone Number: {}".format(search_keyword, phone))

else:
    print("Name not valid")
