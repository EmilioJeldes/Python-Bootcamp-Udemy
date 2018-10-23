# Decorators are functions


def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day")
    
    return wrapper


def greet():
    print("My name is Emilio")


def rage():
    print("IO HATE YOU!")


# # Decorating the function with politeness
# greet = be_polite(greet)
# rage = be_polite(rage)
#
# greet()
# rage()
# WITH DECORATORS THERE'S NO NEED TO DO THIS, JUST WRAP WITH THE DECORATOR

@be_polite
def greet():
    print("My name is Emilio")


@be_polite
def rage():
    print("IO HATE YOU!")


greet()
rage()
