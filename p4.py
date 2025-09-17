# Factors of a number 
#functional decompostion: 1 is the low bound; input is the max bound 
#IB exam needed this code 


# start = 1 
# end = int(input("enter a number: "))
# # numerator / ( {demominator | 1<= demoninator <= input})
# factor_count = 0 
# while start <= end: 
#     results = end/start
#     # start = start + 1 # start += 1<-- same thing 
#     if end % start == 0:
#         print(f"{end} has a factor of {start}")
#         factor_count += 1
#     #print(results)
#     start = start + 1 # start += 1<-- same thing 
# print(f"{end} has {factor_count} factors")
# if factor_count == 2: 
#     print(f"{end} is a prime number.")
# else:  
#     print(f"{end} is a composite number.")

import math 
start = 1
num = int(input("Number please?")) 
new_stop = int(math.sqrt(end)) +1 

while start < new_stop: 
    if end % new_stop==0: 
        dividend = num//start 
        if start != dividend: 
            factor_count += 2 
        else: 
            factor_count += 1 
    start += 1 
print(f"{num} has {factor_count} many factors. ")