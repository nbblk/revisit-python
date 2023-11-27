def hello_world():
    print("Hello world!")

hello_world()

def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int): 
        return
    return print(num1 + num2)

total = sum(1, 3)
print(total)

def multiple_itmes(*args):
    print(args)
    print(type(args))  

multiple_itmes("Dave", "Sara", "John")

def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
multi_named_items(name="Dave", last="gray")


