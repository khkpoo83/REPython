import inspect

def mod1_func1():
    print("Called > ",inspect.getfile(inspect.currentframe()))
def mod1_func2():
    print("Called > ",inspect.getfile(inspect.currentframe()))
