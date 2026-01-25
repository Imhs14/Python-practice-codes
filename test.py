def decorator(func):
    def wrapper(*args, **kwargs):
        print("good Morning")
        result = func(*args, **kwargs)
        print(result)
        print("thanks for using this code")
    return wrapper
@decorator
def func1(x):
    return "hello"+ x
func1("heera")