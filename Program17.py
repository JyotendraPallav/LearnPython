# Program 17 (28) - Print all even and stop once condition is satisfied

def print_even(myList):
    output_List=list()
    for val in myList:
        if val%2==0:
            if val<=237: 
                output_List.append(val)
            else:
                return (output_List)
                break
    return(output_List)
            
import random
Input_List= random.sample(range(300),20)
print("The List of numbers are: ", Input_List)
print("The list of even output is: ",print_even(Input_List))