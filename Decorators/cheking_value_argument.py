from functools import wraps


def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args, **kwargs)
        
        return wrapper
    
    return inner


@ensure_first_arg_is("Burrito")
def fav_foods(*foods):
    print(foods)


print(fav_foods("Burrito", "Ice cream"))
print(fav_foods("ice cream", "burrito"))
