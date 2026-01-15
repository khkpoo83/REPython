import inspect

def mod2_func1():
    print("Called > ",inspect.getfile(inspect.currentframe()))
def mod2_func2():
    print("Called > ",inspect.getfile(inspect.currentframe()))

