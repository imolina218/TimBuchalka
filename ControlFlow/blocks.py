#for i in range(1, 13):
#    print("No. {} squared is {} and cubed is {:4}".format(i, 1 ** 2, i ** 3))
#    print("*"*80)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}?".format(name)))
print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an x on the box")
# else:
#     print("Please come back in {0} years".format(18-age))
if age < 18:
    print("Please come back in {0} years".format(18-age))
elif age == 900:
    print("Sorry, Yoda, you die in the Return of the J edi")
else:
    print("You are old enough to vote")
    print("Please put an X on the box")