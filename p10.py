#string stuff
#tacocat 

def palidrome(word): 
    # checks if argument word is a panlidrome 
    return word == word[::-1]


text = input("fam pls enter word: ")
if palidrome(text):
    print(f"{text} is a panlidrome")
else: 
    print(f"{text} IS BORING~")