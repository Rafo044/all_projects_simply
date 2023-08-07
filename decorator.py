def vurma(func):
    def wrapper(x,y):
        func(x*2,y*2)
    return wrapper

@carp
def topla_vur(x,y):
    print(x+y)

topla(5,10)