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

#####################################################################################################

print('################################################### Method 1: For converting into Plurals #########################################')

import re

def plurals(noun):
    if re.search('[SXZ]$',noun):
        return re.sub('$','es',noun)
    elif re.search('[^aeioudgkprt]h$',noun):
        return re.sub('$','es',noun)
    elif re.search('[^aeiou]y$',noun):
        return re.sub('y$','ies',noun)
    else:
        return noun + 's'

print("Plural: ", plurals(raw_input("Please input the string: ")))
