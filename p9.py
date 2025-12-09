# def Nth(num): 
#     f_0 = 0 
#     f_1 = 1
#     start = 0 
#     while Nth < start: 
#         f_1 = f_0 + f_1
#         f_0 = f_1 + f_0 
#     return     

# nth = input("hello")
# print(Nth(nth))


def fib(nth): 
    if nth in {0,1}:
        return nth 
    else :
        location = 2
        two_before =  0 
        one_before = 1 
        total_sum = 0 
        while location <= nth: 
            total_sum = two_before + one_before
            two_before = one_before 
            one_before = total_sum
            location += 1 
        return total_sum

number = 5 
print(fib(number))
















