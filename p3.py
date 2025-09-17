#donuts 
dounts_count = int(input("enter number of donuts: "))
events = int(input("enter number of events: "))

#we stop when no donuts or no vents 
current_events = 1 #MR PARK USES 0 
while current_events <= dounts_count and events >= 0:
    #as long as the while statments is true it will contiune to loop
    event_type = input("+ or -?")
    donut_amount = int(input("enter donut amount?"))
    if event_type == "+":
        #if the user inputted +
        dounts_count = dounts_count + donut_amount 
        #increasing donut count; by adding donut amount 
        # = assign too
    elif event_type == "-": 
        dounts_count = dounts_count - donut_amount
        #elif means it is connected to the if statment on the top
    else: 
        print("invalid input")
print(f"at the end of our events we have {dounts_count} donuts ")
 
# end of while 

