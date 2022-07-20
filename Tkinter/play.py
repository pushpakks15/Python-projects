def add(*args):
    sum=0
    for n in args:
        sum+=n
    print(sum)

add(1,2,3,4)

def calculate(**kw):
    print(kw)

calculate(add=5,multiply=6,divide=5)