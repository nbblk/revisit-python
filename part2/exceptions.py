class justNotCoolError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

try:
    raise justNotCoolError("just not cool")
#    raise Exception("my exception")
    # print(x)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed")
except NameError:
    print("An name exception occurred")
except ZeroDivisionError:
    print("An zero division exception occurred")
except Exception as error:
    print(error)
else:
    print("No exception occurred")
finally:
    print("gonna rpint with or without exception")