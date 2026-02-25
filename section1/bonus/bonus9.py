password = input("Enter new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for p in password:
    if p.isdigit():
        digit = True
result["digit"] = digit

upper = False
if password.islower() == False:
   upper = True
result["upper"] = upper

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")