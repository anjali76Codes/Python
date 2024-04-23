# In set duplication is not allowed if we write same value more than one time it discarded in the result
#  Set don't have indexing value hence slicing  function we can't use in this 
s1 = {10,34,56,56,89,76,23,12,15}
s2 = {56,46,12,13,15}

# update changes in current set and give updated result
# s1.update(s2)

# here updated set value is display
# print(s1)

#  union is just concating the set but not doing any changes in current set 
# print(s1.union(s2))
# here orginal set value is display
# print(s1) 

#   Even If  the element is not found in the list it not show any error  
# print(s1.discard(20))

# remove is show the error when element is not found in the list
# print(s1.remove(56))
# print(s1)
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s2.issuperset(s1))