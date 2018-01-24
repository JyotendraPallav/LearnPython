# Program 6: Enter File name and print extension
import os

file = raw_input("Please enter Filename: ")
(filename,ext)=os.path.splitext(file)
print(type(file))
print("The Extension is: {0} or to say it better, it is {1}").format(ext,file.split(".")[-1])
