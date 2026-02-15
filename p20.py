def factors(x): 
    results = []
    for i in range(1,x): 
        if x%i ==0: 
            results.append(i)
    return results 

num = int(input())
table = {}
for n in range(2, num+1): 
    table[n] = facotors(n) 
    #changes at everyloop 
    
