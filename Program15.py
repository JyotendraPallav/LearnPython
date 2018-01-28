 # Program 15(26) - To create a histogram
 
def Rep_Str(Val,n):
    for i in range(1,n):
        Val+='*'
    return(Val)
 
def my_histo(my_List):
    for item in my_List:
        print(Rep_Str("*",item))
        # print("\n")

List = input("Please enter numbers: ")
my_histo(List)

# Incomplete one: Needs to correct it