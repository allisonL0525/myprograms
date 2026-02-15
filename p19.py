num = int(input())

our_list = list(range(2,num+1,2))

print(our_list)

# input = 6 
# out put = [2,4,6]


def sixer(seven): 
    if seven[0] == 6 or seven[-1] == 6: 
        return True 
    else: 
        return False 
    