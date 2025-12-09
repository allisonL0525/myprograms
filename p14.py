#creating empty string 
empty_string = ""
ver2 = ''
# determinds if a string is empty 
if not str_var: 
    print("str_var is empty")
 
if len(str_var) == 0: 
    print("str_var is empty")

# format a string to contain dyanamic data 
name = "fluffinton"
str_var = f"hello {fluffinton}!"

#acess individual characters/items in a string 
print(name[0]) #--> F
print(name[-2]) # --> O

#acess the first, acess the last item of a string 
print(name[0]) # prints the first character 
print(name[len(name)-1])# prints the last character
print(name[-1])# prints the last character
#join 2 string together 
a = "poo"
b = "b"
c = a + b #expects poopoo - contacation

#reverse a string 
temp = "park"
reverse_temp = temp[::-1]
v2 = ' '. join(reverse(temp)) # new 

#create a copy of a string 
temp = "hydroflask"
temp_copy = temp [:]
another_copy = temp 

#compares string for equlaity 
a = "marshall"
b = "dog"
 status = a == b # for a string to be equal it has to be equal in numbers and characters 

# determine the min and max value of a string 
temp = "hydroflask"
print(max(temp)) #grab which ever is the lastest 
print(min(temp)) # grab the min
print(max("hello", "goodbye")) # prints the highest --> hello by alphabet 
print(min("1", "2","3"))

# determine if an item or a pattern exsits within a string 
if "poo" in a word: 
    print("there is poo!")

# determines if an item or a pttern within a string 
poop_location = word.find("poo")
poop_location = word word.index("poop")

#locate the index of an item or a pattern occurs within a string 
poop_count = word.count("poo")

# count how often an item or a pattern occurs within a string 
yell_hydroflask = "hydroflask".upper()
calm_hydroflask = yell_hydroflask.lower() #cant have anthing in the brackets 

#convert how often an item or pattern within a string 

# convert a string to an interger 
str_num = "67"
num = "0"
if str_num.isdight(): 
    num = int(str_num)
# determinne if the string can be convert into an interger 

#determines if a string contains alphabetical characters 
word = "shsm".isalpha()

#remove non-alphabetical characters from a string 
    # somtimes it is esaier to create then remove 
gibberish = "123fsdfghjkdmdfulmnp;"
clean = ""
i = 0
while i < len(gibberish): 
    if gibberish[i].isalpha(): 
        clean  += gibberish[i]
    i += 1
#remove all alphabetical charachters from a string 
gibberish = "123fsdfghjkdmdfulmnp;"
clean = ""
i = 0
while i < len(gibberish): 
    if gibberish[i].isalpha() == False: 
        clean  += gibberish[i]
    i += 1
#remove all whitespace from string 
example = "h hf  ja  p fj r   e h      q"
example = example.replace(" ", "") #cleans whitespace

#sort a string n ASCII order of reverse ASCII order 

# determine if a string follows a ruleset 