from functools import wraps


def enforce(*types):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # convert args into something mutable
            new_args = []
            for (a, t) in zip(args, types):
                new_args.append(t(a))
            return fn(*new_args, **kwargs)
        
        return wrapper
    
    return decorator


@enforce(float, float)
def divide(a, b):
    print(a / b)


divide(4, 6)
divide(4, '2')
divide(4.5, '2')
divide("asd", '2')
