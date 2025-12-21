#l1=[]
#l=[5,10,15,20,25]
#for num in l:
#    print(num)
#    if num>15:
#        l1.append(num)
#print(l)
#print(l1)
# Each loop iteration gives a single element, not the whole list.
# Compare and append using the loop variable, not the list itself.

#LIST 

l1=[5,10,15,20,25]
l=[num for num in l1 if num>15]
print(l)

# For each element, keep it if greater than 15,



# WITHOUT ELSE(filtering):
# Syntax: [expression for item in iterable if condition]
# Reason: Elements that fail the condition are skipped (removed), so no else is needed.
# WITH ELSE(transformation):
# Syntax: [expression_if_true if condition else expression_if_false for item in iterable]
# Reason: Every element must produce a value, so else is mandatory.
