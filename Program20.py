# Program 20 (81- 107)
#     To Concatenate N Strings
#     numbers greater than all numbers in a list
#     To check if String is numeric
#     File path is a file or a directory
#     To get system time
#     Access and print URL content
#     To get System command Output
#     Extract Path, filename and extension from a path
#     retrive file properties
    

# Solution: 1 

def Add_Strings(N):
    Final_Str=""
    for i in range(0,N):
        Final_Str+=raw_input("Please input the string to be added: ")
    
    return Final_Str

print("Your combined String is {0}".format(Add_Strings(input("Enter # of Strings: "))))

# Solution: 2

import random
Rand_list=random.sample(range(1000),25)

number_to_check = input("Enter the number to compare: ")
# Rand_list.sort(reverse=True)
if number_to_check>max(Rand_list):
    print("this number is larger than list with list being: ",Rand_list)
else:
    Filtered_list=[number for number in Rand_list if number>number_to_check]
    print("Your filtered list is: {0}\n where initial list was {1}".format(Filtered_list,Rand_list))


# Solution: 3

Text_to_check=raw_input("Please input the string to be checked for numeric: ")
print(unicode(Text_to_check,'utf-8').isnumeric())

# Solution: 4

import os.path
# FilePath= os.path.join('D:\Github','Python Tutorial','LearnPython')
for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))

# Solution: 5

import time
import datetime
structtime=time.localtime()
print(datetime.datetime(*structtime[:6]))
print(time.ctime())

# Solution: 6
print("Not Read yet for 6th problem")


# Solution: 7
print("Not Read yet for 7th problem")

# Solution: 8
import os
(Path,ext)=os.path.splitext(os.path.abspath(__file__))
print("root of the file is {0} and extension of the file is{1}".format(Path,ext))