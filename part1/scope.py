name = "Dave"
count = 1

def another():
    color = "blue"
    global count
    count += 1
    print(count)    

    def greeting(name):
        color = "red"
        print(name)
        print(color)

    greeting("John")
# print(color)

another()