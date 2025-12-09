#linear search 

def str_lin_search(text, target):
     #mutli var function
    if not text : # len(text) == 0 
        return -1 
    else: 
        i = 0 
        while i < len(text): 
            if text[i] == target: 
                return i 
            i += 1
        #end of while 
        return -1 

print ("jasper... where is p?", str_lin_search("jasper","p"))

    
