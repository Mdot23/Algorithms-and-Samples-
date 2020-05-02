# Filter a given array of integers and output only those values that are more or equal to the specified value 

# 1. Iterate over the collection, 
# 2. Compare the collection current item with x, 
# 3. Push this element to the resultArray if it pass the condition.

collection = [
  { name: 'WF1', Millisecond: 43 },
  { name: 'WF2', Millisecond: 21 },
  { name: 'WF3', Millisecond: 30 }
]

  
def filterArray x, collection
  resultArray = [];
  # For i in array[:Millisecond]; if i is == to integer then perform operation  
  collection.select do |elem|
      if elem[:Millisecond] >= x
          resultArray.push(elem[:Millisecond])
          return resultArray
      end
  end
end
    



