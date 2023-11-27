# dictionaries
# dictionaries are a data structure that stores key-value pairs

band = {
    "vocals": "Plant",
    "guitar": "Page",
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(type(band2))

# access data
print(band["vocals"])
print(band.get("vocals"))

print(band.keys())
print(band.values())

# as tuples
print(band.items())

# verify
print("guitar" in band)
print("triangle" in band)

band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)


print(band.pop("bass"))
print(band)


band["drums"] = "Bonham"
print(band)

print(band.popitem()) # tuple
print(band)

# delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictionaries

# band2 = band # create a reference
# print("bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)


band2 = band.copy()
band2["drums"] = "Dave"
print("good copy!")
print(band2)
print(band)

# or use the dict() constructorfunction
band3 = dict(band)
print("good copy!")
print(band3)


# nested dictionaries

member1 = {
    "name": "Robert",
    "instrument": "bass"
}
member2 = {
    "name": "Jimmy",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])


# Sets
# sets are a data structure that stores unique values

nums = { 1, 2, 3, 4 }
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# no dups allowed
nums = { 1, 2, 3, 4, 1, 2, 3, 4 }
print(nums)


# True is a dupe of 1, false is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

print(2 in nums)

# but you cannot refer to an item by index

nums.add(8)
print(nums)

morenums = { 5, 6, 7, 8, 9, 10 }
nums.update(morenums)
print(nums)

# mere two sets to create a new set
one = {1,2,3}
two = {6,7,8}
mynewset = one.union(two)
print(mynewset)

one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)
print(one)

one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)


