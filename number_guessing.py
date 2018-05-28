import random

magic_numbers = random.randint(0,9)
chances = 3

print("{}".format(magic_numbers))

for attempt in range(chances):
    print("Attempt number: {}".format(attempt+1))
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number ==  magic_numbers:
        print("You got the number right!")
    if user_number !=  magic_numbers:
        print("You didn't quite get it!")

print ("\n\n Coorect answer was: {}".format(magic_numbers))
