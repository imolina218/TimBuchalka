available_courses = [1, 2, 3, 4, 5, 6]
user_input = ""
user_name = ""

while user_input not in available_courses:
    user_name = input("What is your name ?")
    print("//Hi {} please choose the number that correspond to the course that you want to take:"
          "\n> 1. C#"
          "\n> 2. Python 3.0"
          "\n> 3. Java"
          "\n> 4. R"
          "\n> 5. Kotlin"
          "\n> 6. C++".format(user_name))
    user_input = int(input("Please choose a course: "))

while user_input > 0:
    if user_input == 1:
        print("Welcome {} to the C# course".format(user_name))
        break
    elif user_input == 2:
        print("Welcome {} to the Python 3.0 course".format(user_name))
        break
    elif user_input == 3:
        print("Welcome {} to the Java course".format(user_name))
        break
    elif user_input == 4:
        print("Welcome {} to the R course".format(user_name))
        break
    elif user_input == 5:
        print("Welcome {} to the kotlin course".format(user_name))
        break
    elif user_input == 6:
        print("Welcome {} to the C++ course".format(user_name))
        break
