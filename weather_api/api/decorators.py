from functools import wraps


def say_hi(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        print('Hello, This is wrapped by my custom decorator!')
        return function(request, *args, **kwargs)
    return wrap