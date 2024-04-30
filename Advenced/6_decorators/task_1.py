import time

def log(func):
    def wrapper():
        print(f"- called function: {func.__name__} at {time.strftime('%X')}")
        func()
        print(f"- finished function: {func.__name__} at {time.strftime('%X')}")
    return wrapper

@log
def hello():
    print("hello")

hello()
