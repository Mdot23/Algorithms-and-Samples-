# dict.get returns value for the given key. If no key, returns None
# First for loop stores the occurred characters and their corresponding frequencies
# Second loop is to loop over the string sequence again if the next character exists and the# number of occurrences is 1, then return this character’s index. Otherwise, returns -1. 
# Using this method, we find the first unique character in a string.
"""
1. Pass string_data to function 
2. Create dictionary to store input string 
3. itterate over elements in string_data 
4. Implement counter 
5. Loop over string again using enumerate as counter to determine if character exists 
"""

def first_uniqchar(string_data):

        data = {}
        
        for char in string_data:
            data[char] = data.get(char, 0) + 1
            
        for i, n in enumerate(string_data):
            if data[n] and data[n] == 1:
                return i
        
        return -1
