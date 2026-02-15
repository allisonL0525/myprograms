# Non destructive selsection sort with lists

# function said 
# 1 arguement 
# colon ends it 
def select(a_list): 
    if len(a_list) <= 0:
        return a_list
        # returns it as there is nothing 
    else: 
        #guarantee that there is somehting in there 
        i = 0 
        while i < len(a_list): 
            smallest = a_list[i] # the prove it is or it is not 
            # let go hunting 
            j = i+1  # search for i +1 pnwoards 
            new_location = i 
            while j < len(a_list): 
                new_value = a_list[j]
                if new_value < smallest: 
                    # if new vlaue isnt the smallest number 
                    smallest = new_location
                    new_location = j 

            #ennd of hunting 
            # swap smallest into proper location 
            temporary = a_list[i]
            a_list[i] = smallest
            a_list[new_location] = temporary
            # this is how we executed a swap in most lanagues that has mutable langugues 
            # the python way to swap location 
            a_list[i], a_list[new_location] = a_list[new_location], a_list[i]
            i += 1 
            #access each value in current value
            #smallest --> put in correct location 
