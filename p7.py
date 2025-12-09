def search(numb,max,min):
    cheese = 0 
    while cheese != numb: 
        if max //2 > numb: 
            cheese = range(max//2,min)
        elif max // 2 < numb: 
            cheese = range(max,max//2)
        else: 
            return cheese 

mac = (input("whats the number?"))
print(search(a,b,c))



 
def cheese(numb_list,target ): 
    for i in numb_list: 
        a = numb_list - 1
        if a in numb_list == target:
            return numb_list
    return False
#method 1
# method 3 --> liinear search 
for i in range(a_list): 
    diff = target - a_list[i]
    for j in range(i+1, len(a_list)): x#makes sure that the values arent repeated
        if a_list[j] == diff: 
            print(f"{target} is at {i},{j}")
# method 3 with binary serarch 
    # with binary search since a_list is guaranteed to be sorted 

#method 5 beats all the previous methods --> uses 2 pointers 
def cheese(numb_list,target): 
    j = len(numb_list) - 1 
    i = 0   
    while i < j: 
        if target[j] + target[i]> target: 
            j -= 1 
        elif target [j] + target [i] < target: 
            i += 1 
        elif target[j] + target == target: 
            return True 
        else: 
            return False
    return False 


        