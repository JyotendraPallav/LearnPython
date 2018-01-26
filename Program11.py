# Program 11(19) - To find Is

def As_Is(Val):
    if(Val.find('Is')==0):
        return Val
    else:
        return('Is'+Val)

Str=raw_input("Input a string: ")
print(As_Is(Str))