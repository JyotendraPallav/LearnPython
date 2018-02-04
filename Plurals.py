# Program copied from book of chapter Closures and generators for 
# converting nouns into plurals

# printing fibonacci series

from __future__ import print_function

def fib(max):
    a,b=0,1
    while a<max:
        yield a
        a,b=b,a+b

# for n in fib(1000):
#     print(n,end=' ')

print(list(fib(1000)))