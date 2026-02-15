#bubble sort 
def bubble(list_a): 
    if len(list_a) <= 0: 
        return list_a
    else: 
        i = 1 
        j = i - 1 
        while i <len(list_a):
            if j in range(1, list_a[i]): 
                list_a[j], list_a[i] = list_a[i], list_a[j]     
                i = i + 1 
                j = 1 + i 
    return list_a   
        


a = [1, 8, 7, 5, 3, 2, 5]
print(bubble(a))


# def bubble_sort(list_a):
#     n = len(list_a)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if list_a[j] > list_a[j + 1]:
#                 # Swap if the element found is greater than the next element
#                 list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]
#     return list_a

# a = [1, 8, 7, 5, 3, 2, 5]
# print(bubble_sort(a))



