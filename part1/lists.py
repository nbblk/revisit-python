users = ['Diana', 'James', 'John', 'Mary', 'Sara']

data = ['Data', 42, True]

emptylist = []

print("Dave" in users)


print(users[0])
print(users[-1])
print(users[-2])
print(users.index('Sara'))
print(users[0:2])
print(users[-3:-1])

print(len(data))

users.append('Elsa')
print(users)

users += ['Jason']
print(users)

# users.extend(['Robert', 'Jimmy'])
# print(users)

# users.extend('Robert')
# print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['eddie', 'alex']
print(users)

users[1:3] = ['Robert', 'JPJ' ]
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = 'dave'
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,42, 78, 1, 6]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]


print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "neil" , True])
print(mylist)


# tuples

mytuple = tuple(['dave', 42, True])

anothertuple = (1,4,2,8)

print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(w,*x,y,z) = anothertuple
print(w)
print(x)
print(y)
print(z)
print(anothertuple.count(4))