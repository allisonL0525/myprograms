# ahhhhhhhh

place = 1 

while True: 
    dice = int(input("hey kid, whats your dice roll: "))
    if dice > 6: 
        print("please use 1 dice")
    elif dice < 1: 
        print("ermmm...")
    if place + dice  > 100:
        break 
    
    elif place + dice < 100: 
        new_place = place + dice 
        game_dict = {
        9:34,
        54:19,
        40:64,
        90:48,
        67: 86,
        99:77
    }
    if place in game_dict: 
        place = game_dict[place]
        print(new_place)
    else: 
        print(new_place)



    # if dice > 6: 
    #      print("please use 1 dice")
    # elif dice < 1: 
    #     print("ermmm...")
    # else: 
    #     place = place + dice
    #     print(f"your currently at {place}") 
    #     if place == 40: 
    #         place = 64 
    #         print(f" you have move to {place}")
    #     elif place == 9: 
    #         place = 34
    #         print(f" you have move to {place}")
    #     elif place == 67:
    #         place = 86
    #         print(f" you have move to {place}")
    #     elif place == 54: 
    #         place = 90
    #         print(f" you have move to {place}")
    #     elif place == 99:
    #         place = 77
    #         print(f" you have move to {place}")
    #     elif place == 100: 
    #         print("you won")
    #         print(f" you have move to {place}")
    #         break
    #     elif place > 100: 
    #         place = place - dice
    #         print ("you cant move")





