#chore List 

time = int(input("whats the total time? "))
total_chores = int(input())
chore_times = []

for x in range(total_chores): 
    x = int(input("whats the time it takes to get them done?"))
    chore_times.append(x)

chore_times = sorted(chore_times)

value = 0 
counter = 0
for i in range(1, len(chore_times)): 
    counter += 1 
    value += chore_times[i]
    if value > time: 
            break 

print(f"you can complete {counter} chores")
        

# Mr park solution
# setup 
time_left = int(input())
chores = int(input())
time_per_chore = []
for i in range(chores): 
    time_per_chore.append(int(input()))

#Maximizing chores 
# step 1 - sort choices from least to greatest 
time_per_chore.sort() #on IB exam use a sort mechanism (bubble)
# based on merge sort 
chore_ctr = 0 
i = 0 

while time_left > 0 and i < len(time_per_chore): 
    if time_per_chore[i] <= time_left: 
        time_left -= time_per_chore[0]
        chore_ctr+= 1 
        # time_per_chore.pop(0) # why are .remove? 
        i+= 1 
    else: 
        break 




