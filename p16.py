#1. create an empty string 
a_list = []
b_list = list()
#2. determine if a string is emmpty 
if not a_list: 
    print("it is empty")

if len(a_list) == 0: 
    print("it is list")
#3. what does len(), sum(), max() do when a list is an argument? 
c_list = [3,1,4,5,9]
print(len(c_list)) # gives 6 
print(sum(c_list)) # gives 23 
print(max(c_list))
print(min(c_list))
#4. Access individual charachters/items in a list 
d_list = list("hello, world!") # 13 indivdual string 
print(d_list[0]) # "h "
print(d_list[-1]) #"!"
print(d_list[1:4]) # ["e',"l", "l" ]
#5. access the first, access the last item in a list 
a = ["3","1","4"]
b = ['Marshall', 'freya','joy']
c = a + b # creates new list with a and b 
a.extend(b) #mutates a to give the contents of b  
a = ["3","1","4"]
for item in b: 
    a.append(b)
#6. join two/mutiple list together 

#7. reverse a list (2 ways)

#8 create a cop if a list 

#9. compare list for equaility 

#10. determine if an item exist form a list 

#11. locate the index of an item within a list 

#12. count how often a item occurs within a list 

#13. covert a string to a list 

#14. sort a list 

#15. sort 2 list where the indez are attached to each other 