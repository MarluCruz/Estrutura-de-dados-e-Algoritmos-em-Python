def function1():
    print("Case 1 selected")

def function2():
    print("Case 2 selected")

def default():
    print("Value default")

def switch(case):
    if case == "1":
        return function1
    elif case == "2":
        return function2
    else:
        return default

if __name__ == "__main__":
    function = switch(case="1")
    function()
    