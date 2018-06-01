


def user_input():
    user_tip_csv = input("Enter your six numbers, separated by comma: ")
    
    #input control
    print(user_tip_csv)


    #enter user numbers into set
    user_tip_set = set()
    user_tip_set = (user_tip_csv.split(","))

    print(user_tip_set)


user_input()
