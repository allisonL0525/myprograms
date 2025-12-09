# a = [3,1,4,5,1,9]
# b = a 

# b[-1] = "pooo"
# print(a)
# print(b)

# current_code = input("add current code: ")
# new_code = ""
# i = 0 
# for x in current_code: 
#     if x.isalpha():
#         if x.isupper(): 
#             new_code+= x
#     elif x.isdigit(): 
#         x = int(x)
#         i = i + x 

# print(new_code+ str(i))


# PRODUCT CODES 
def cleaner_code(text): 
    uppercase = ""
    postives = ""
    negatives = ""
    total_sum = 0 
    for item in text: 
        print(item)
        if item.isalpha() and item.isupper(): 
            uppercase += item 
            if len(postives) > 0: 
               total_sum += int(postives)
               postives = ""
            if len(negatives) > 0:
                total_sum += int(negatives)
                negatives = ""
        elif item == "-": 
            if len(negatives) > 0:
                total_sum += int(negatives)
                negatives = "-"
            else: 
                negatives = "-"
        elif item.isdigit(): 
            if len(negatives) > 0: 
                negatives += item 
            else: 
                postives += item 

         #print item        
         # end of for loop
    if len(postives) > 0: 
        total_sum += int(postives)
    if len(negatives) > 0: 
        total_sum += int(negatives)
    product_code = upper_code + str(total_sum)
    return product_code


inp = input("what your code: ")
print(cleaner_code(inp))