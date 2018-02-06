# Program copied from book of chapter Closures and generators for 
# converting nouns into plurals

# printing fibonacci series

from __future__ import print_function
import random

def fib(max):
    a,b=0,1
    while a<max:
        yield a
        a,b=b,a+b

# for n in fib(1000):
#     print(n,end=' ')

print("Here comes your fibonacci series - \n{0}".format(list(fib(random.Random(3000)))))

#####################################################################################################
import re
def build_match_and_apply_function(pattern,search,replace):
    
    def match_word(word):
        return re.search(pattern,search)
    def apply_word(word):
        return re.sub('$',replace,word)
    return (match_word,apply_word)

def rules(rule_filename):
    with open(rule_filename) as pattern_file:
        for line in pattern_file:
            pattern,search,replace=line.split(None,3)
            yield build_match_and_apply_function(pattern,search,replace)

def plurals(noun,rule_file='plural4-rules.txt'):
    for match_name,apply_name in rules(rule_file):
        if match_name(noun):
            return apply_name(noun)
    raise ValueError('No matching rule for {0}'.format(noun))
    
print("Here is your plural: {0}".format(plurals(raw_input("Enter the noun to convert into Plural: "))))