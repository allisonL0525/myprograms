# Roberta the Golfing robot 



distance = int(input(""))
clubs = int(input())
list_distance = []

for range(clubs): 
    x = input("whats the distance")    
    list_distance.append(x)

clubs = sorted(clubs)

def math(result,distance): 
    counter = 0 
    hit = 0
    i = 0
    while i < len(result)
        counter +=1 
        if hit += result[i] == distance: 
            return counter 
        elif hit += result[i] < distance: 
            return "Roberta Loses"
        else:  
            i+=1



#dynamic programming 

import math 

def golf(clubs,target):
    distance = [0] + [math.inf] * target 
    for current in range(len(distance)): 
        for c in clubs: 
            new_loc = current + c 
            if new_loc <= target: 
                distnace[new_loc] = min(distance[current] +1, distance[new_location])
    return distance[target]

print(golf([3,1,4],15))


# def sort_club(clubs):  
#     result = []
#     while len(clubs)> 0: 
#         val = max(clubs) 
#         result.append(val)
#         clubs.remove(val)
#     return  


