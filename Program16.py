# Program 16(27) - Concatenate items of a list

def con_list(mylist):
    print (mylist)
    big=""
    for index in mylist:
        big+=str(index)
    return big

print(con_list(list(raw_input("Please input your list of strings: "))))