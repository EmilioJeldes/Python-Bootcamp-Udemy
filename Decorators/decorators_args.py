# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#
#     return wrapper


def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    
    return wrapper


@shout
def greet(name):
    return f"Hi, im {name}"


def order(main, side):
    return f"Hi, IO'd like the the {main}. with a side of {side}, please"


@shout
def lol():
    return "LOL"
