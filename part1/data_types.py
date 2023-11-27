import math

# stirng data type

# literal assignment
first = "Dave"
last = "Gray"


# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))


# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#casting number to a strring
decade = str(1990)
print(type(decade))

statement = " i like rock music from the " + decade + "s."
print(statement)

# multiple lines
multiline = '''
    hey, how are u
    i was just checking in...
    i hope you are doing well
    
'''

print(multiline)

# escaping special characters
sentence = 'i\'m back at work!\they!\n\nWhere\'s this at\\located?'
print(sentence)



# string methods
print(first)
print(first.lower())
print(first.upper())
print(first.capitalize())

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                      "
multiline = "good morning!              " + multiline

print(len(multiline))


print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1". rjust(4))
print("Muffin".ljust(16, ".") + "$1". rjust(4))
print("Cheesecake".ljust(16, ".") + "$1". rjust(4))


print("")


# string index values
print(first[1])
print(first[-1])
print(first[0])
print(first[1:-1])
print(first[0:4])

# some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

# boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(x, bool))

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 6+4j
print(comp_value.real)
print(comp_value.imag)

# built-in functions for numbers
print(abs(gpa))  
print(round(gpa * -1))
print(round(gpa, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# error if you attempt to cast inccorect data
# zip_value = int("newyork")