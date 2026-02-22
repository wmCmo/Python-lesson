#how to find the list of all methods that can be applied 

password = input("Enter the password:")
num = 0

while password != "takoyaki":
    num += 1
    print(f"{num} times you wrong password, try again.")
    password = input("Enter the password:")
