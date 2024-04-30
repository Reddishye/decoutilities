# @singleton
# Make a class a singleton. Only one instance of the class will be created and returned.

def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


# @private
# Make a class private and raise an exception if it is accessed from outside the module.

def private(cls):
    def wrapper(*args, **kwargs):
        raise Exception("This class is private and cannot be accessed from outside the module!")
    return wrapper

# @static
# Make a class static and raise an exception if it is instantiated. (EXPERIMENTAL)

def static(cls):
    def wrapper(*args, **kwargs):
        raise Exception("This class is static and cannot be instantiated!")
    return wrapper

# @threaded
# Make a class threaded and return a thread object. (EXPERIMENTAL)

def threaded(cls):
    import threading

    def wrapper(*args, **kwargs):
        return threading.Thread(target=cls, args=args, kwargs=kwargs)
    return wrapper

# @trycatch
# Make a piece of code try-catchable without using try-catch blocks.
def trycatch(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrapper