# name = input("What is your name?")
# num = 0
# while num < 6:
#     print(name.capitalize())
#     num += 1

# greeting = "hello"
# print(greeting.upper())

countries = []

while True:
    country = input("Enter the country: ")

    if country == "quit":
        break
    countries.append(country)
    print(countries)


