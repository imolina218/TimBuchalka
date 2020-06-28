name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age >= 18 and age < 31:
    print("Welcome to the holiday {}".format(name))
else:
    if age < 18:
        print("Sorry {0}. Your age is not allowed at this holiday, come back in {1} years.".format(name, 18-age))
    else:
        print("Sorry {}. You are too old for this holiday.".format(name))