import random

def ask_user_and_check_reply():
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number ==  magic_numbers:
        return ("You got the number right!")
    if user_number !=  magic_numbers:
        return ("You didn't quite get it!")

magic_numbers = random.randint(0,9)

def run_program_x_times(chances):
    for attempt in range(chances):
        print("Attempt number: {}".format(attempt+1))
        message = ask_user_and_check_reply()
        print(message)



run_program_x_times(int(input("How many tries do you want to have?")))

print ("\n\n Coorect answer was: {}".format(magic_numbers))
