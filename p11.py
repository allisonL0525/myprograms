#string cleaner 
def clean(text): 
    result = ""
    i = 0 
    #i for index, avoid index cuz it is a fucntion/method name 
    while i < len(text): 
        if text[i].isalpha(): 
            result = result + text[i].lower()
            #returns if the given character is alphabetically 
        i+= 1
    return result

h = input("insert it here pls")
print(clean(h))

#linear search 