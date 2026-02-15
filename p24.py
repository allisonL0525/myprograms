def zero_finder(a_list):
    zeros = []
    non_zeros = []
    for i in a_list: 
        if i == 0:
            zeros.append(i)
        else: 
            non_zeros.append(i)
    return non_zeros + zeros 


        
def movezreos(nums): 
    temp = [0] * len(nums)
    i = 0
    for num in nums: 
        if num != 0: 
            temp[i] = num
            i += 1 
    nums = temp 

def movezero3(nums): 
    zero_1 = 0
    for i in range(len(nums)): 
        if nums[i] != 0: 
            nums[i], nums[zero_1] = nums[zero_1], nums[i]
            zero_1 += 1 
    return nums #unnescessary 



a = [0, 1, 3, 0, 12]
print(movezreos(a))


# solution 1 and 2 uses more mermoy --> making an empty list and a new varaible 
# complextiy is about less mermory and less lines 
