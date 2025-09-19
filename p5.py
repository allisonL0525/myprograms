#heads or tails 

from random import choice 
# choice --> function that randomly chooses from a list 

while True:
    print("welcome to our heads or tails game!")
    print("please choose either heads or tails")
    while True: 
        user_input = input("Whats your choice: ")
        user_input = user_input.lower() #makes everthing lowercase
        #immutability --> data/object that cannot be mutated
        # strings cannot be change unless told so

        if user_input in ("heads", "tails", "tail", "head"):
            #user_input was valid, we can exit the while loop
            # in --> membership checker 
            break # allows us to exit a looping structure
            # only way to exit the loop
        else:
            print("please input heads or tails :)")
    #end of while

    flip_results = choice(["heads", "tails"])
    print(f"the computer guessed{flip_results}")
    if user_input in {"heads", "head"} and flip_results == "heads":
        # condition: user_input in {"heads", "head"}
        # and --> logical AND
        # condition flip_results == "heads"
        # condtion + condition 
        # and/or are only for combing conditions, if not truthy falsey is bad
        print("the user guessed correctly")
    elif user_input in {"tails", "tail"} and flip_results == "tails":
        print("the user guessed correctly")
    else: 
        print("please dont gamble!")
    
    user_input = input("want to exit: YES/NO")
    if user_input.lower() == "yes":
        break 
    else: 
        print("ok")
