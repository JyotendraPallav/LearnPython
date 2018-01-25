# Program 7: Convert a number tuple into Date String

Dates=input("Please input day, month, year: ")
print(type(Dates))
print("Or, The Examination Date would be:%i/%i/%i "%Dates)
print("Or, The Examination Date would be:{0[0]}/{0[1]}//{0[2]} ").format(Dates)