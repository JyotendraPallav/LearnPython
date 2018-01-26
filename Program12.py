# Program 12(20) - Repeat a string n Times

def Rep_Str(Val,n):
    for i in range(1,n):
        Val+=Val
    return(Val)

String =raw_input("Enter The String: ")
Rep = input("Please input repition: ")

print(Rep_Str(String,Rep))