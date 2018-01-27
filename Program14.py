# Program 14(24) - to copy n time first 2 val of string

def Rep_Str(Str,n):
    Val=Str[0:2]
    for i in range(1,n):
        Val+=Val
    return(Val)

String =raw_input("Enter The String: ")
Rep = input("Please input repition: ")

print(Rep_Str(String,Rep))