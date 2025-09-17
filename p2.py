#Roller coaster 
#input 
place_in_line = int(input())
num_cars = int(input())
capacity = int(input())
#keep the input() blank

#processing 
total_capacity = num_cars * capacity

if total_capacity >= place_in_line:
    print("yes")
else: 
    print("no")