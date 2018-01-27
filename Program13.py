# Program 13 (22) - Count the number of 4 in a list
import random
# In_List=random.sample(range(15),15)    Used for Random allocated number

# import numpy as np
# In_List = np.random.choice(10,10,replace=True)  # Used for Random numbers with repition

In_List=[random.randrange(10) for i in range(20)]

counter=input("Please input the number for counting in random list: ")
print("The number of occurence for %i in %r is: %i"%(counter,In_List,In_List.count(4)))


# np is ndaraay - Will deal with it later but for now, count function counts occurence in 
#a list (Gyaan)