def anagram(word1,word2):
    # cheese = dict.fromkeys(words)
    # if len(word) = 0: 
    #     return False
    # if len(word) == 2
    # assuming word1, word2 are cleaned 
    # all uppercase, no special characters, no numbers 
    # technique --> frequency table 
    freq_table = {}
    for c in word1: 
        if c in freq_table: 
            freq_table[c]+ 1
        else: 
            freq_table = 1
    for c in word2: 
        if c not in freq_table: 
            return False 
        # not a unique character in word 1 --> doesnt exsits 
        else: 
            freq_table[c] -= 1 
            # we have accounted for it 
            # looking for character in frequency table and goes back
            if freq_table[c]<0: 
                return False 
                # if a characters esxsits to too much and ex poop and poopoo
    for key, value in freq_table.items(): #method that belongs to dictonaries 
    # return values frist, then address 
    # acts like a fail save 
        if value != 0: 
            return False
    return True

#  word1 = "poo"
#     freq_table = { 
#         "p" : 1
#         "o" : 2
#     }
# word2 = "poopoo"
#     freq_table

#trig identies hahha
    
