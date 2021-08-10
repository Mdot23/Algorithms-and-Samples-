# List Comprehension Examples ||| list = [expression for the elements in the iterable]
# 1 
squares = [i**2 for i in range(1, 10)]
remainders = [x**3 % 11 for x in range(1,101)] 

# Compute cartesian product 
Accounts_1 = [123456789102, 921453789102, 173459989102, 573116729002]
Accounts_2 = [520615910315, 124016222416, 772014519321, 981344436621]

cartesian_product = [(a,b) for a in Accounts_1 for b in Accounts_2]

# Increment using List Comprehension instead of map || This will return a list whereas map will reutrn map object 
account_id = [123456789102, 921453789102, 173459989102, 573116729002]
account_id_2 = [520615910315, 124016222416, 772014519321, 981344436621]

def increment_account_id(account_id):
    return account_id + 1

final_output = [increment_account_id(i) for i in account_id]

# Mapping objects 
account_id = [123456789102, 921453789102, 173459989102, 573116729002]
account_id_2 = [520615910315, 124016222416, 772014519321, 981344436621]

def increment_account_id(account_id):
    return account_id + 1

final_output = map(increment_account_id, account_id)
list(final_output)

# Conditionals | Can also add conditionals at the end of a list comprehension
# In this example, thi will filter out anyone words that aren't the keyword value best 
sentence = 'Milton is the best'
keywords = [i for i in sentence if i in 'best']

# For changing a value instead of filtering it out, it's best to place conditional in beginning of expression
home_prices = [230000, 500000, 650000, 100000, 520500, 230500, 800500]
budget_filter = [i if i < 500000 else 0 for i in home_prices]
budget_filter
# Can also create a Function for this 
def get_price(price):
    return price if price < 500000 else 0
prices = [get_price(i) for i in home_prices]
prices

# Set Comprehension 
message = "The acccount id 123456789123"
filter = {i for i in message if i in 'id'}
filter



