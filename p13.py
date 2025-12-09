def anagram1(one):
    x = one.lower()
    x = sorted(x)
     

def anagram2(two):  
    y = two.lower()
    y = sorted(y)
    

hi = input("hey input word 1: ")
hello = input ("input word 2:  ")

hi = anagram1(hi)
hello = anagram2(hello)

if hi == hello: 
    print("true")
else: 
    print("false")

def alpha_sorting(text): 
    abc = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    i = 0 
    while i < len(abc): 
        current_letter = abc[i]
        text_lowered = text.lowered()
        if current_letter in text_lowered: 
            result = result + current_letter().count(current_letter)
        # if abc[i] in text.lower():
        #     result += abc[i]*text.lower().count(abc[i])
        i += 1 
    return result
            
    