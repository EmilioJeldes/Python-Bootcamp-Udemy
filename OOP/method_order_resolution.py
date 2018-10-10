# MRO
class A:
    
    def do_something(self):
        print("Method defined in: A")


class B(A):
    
    def do_something(self):
        print("Method defined in: B")


class C(A):
    
    def do_something(self):
        print("Method defined in: C")


class D(B, C):
    pass
    # def do_something(self):
    #     print("Method defined in: D")


# print(D.__mro__)
# print(D.mro())
# print(help(D)) => human reading


thing = D()
thing.do_something()

#     A
#   /   \
#  B     C
#   \   /
#     D

# D, B, C, A, Object
