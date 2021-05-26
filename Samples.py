# Reverse lookup function. This will take a value and return the first key that maps to that value.
def rever_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError



# Inverts a dictionary 
"""
Through the loop, key gets a key from d and val gets corresponding value. If value is not in inverse,
we create a new item and initialize it with a singleton."""

def invert_d(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse 


""" This will return True if a duplicate element is in the list otherwise it will return False""" 
def duplicate(v):
   """If duplicate in list returns True else returns False"""

   d = {}
   for i in v:
       if i in d:
           return True
       d[i] = True
   return False 




# Using zip for tuple assignment 
Stage = [('a', 'PROD'), ('b', 'INTEG'), ('c', 'DevTest')]
Stage2 = [('d', 'TEST')]
def has_match(Stage, Stage2):
    for x, y in zip(Stage, Stage2):
        if x == y:
            return True
    return False

# Using enumerate to traverse elements + indicies 
for index, element in enumerate('123'):
    print(index,element)



# Sort elements in list from shortest to longest 
words = ["PROD", "TESTING", "BETA"]
def sort_by_length(words):
    l = []
    for word in words:
        l.append((len(word), word))
    
    l.sort(reverse=True)

    res = []
    for length, word in l:
        res.append(word)
    return res 

# Itterate through a LISTS of Dictionaries. Example givien = ['Value'{'Dictionariy key: 'Dictionary Value'}...]
for index in range(len(datalist)):
    for key in datalist[index]:
        print(dataList[index][key])
