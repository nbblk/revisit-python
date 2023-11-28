import os
# r = read
# x = create
# w = write
# a = append


f = open("names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readLine())
# print(f.readLine())

for line in f:
    print(line)


f.close()


try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("something went wrong")
finally:
    f.close()

# append when it doesnt exist

f = open("names.txt", "a")
f.write("Neil")
f.close()
f = open("names.txt")
print(f.read())
f.close()


# write when it doesnt exist
f = open("context.txt", "w")
f.write("I delete all of the context")
f.close()

# f = open("context.txt", "r")
# f.write(f.read())
# f.close()


f = open("names.txt", "w")
f.close()

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("file does not exist")


with open("names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)