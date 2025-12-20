#squares =[]
#for i in range(6):
#    squares.append(i*i)
#print(squares)

# [ output for item in iterable if condition(optional)]

# LIST COMPREHENSION
sq =[i*i for i in range(6)]
print(sq)
sq1 =[j*j for j in range(6) if j%2 != 0] #square of odd numbers only
print(sq1)

nums=[-2,-3,3,4,-1,7]
nums = [0 if val<0 else val for val in nums] # replacing negative no wiyh zero
print(nums)

words =["hello","python","apnacollege"]
print(words[0].upper())
words=[val.upper() for val in words]
print(words)
