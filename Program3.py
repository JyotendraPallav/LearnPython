'''Writing Program 3 - Finding current date and time'''
import time
print("Current Date and time is:",time.asctime(time.localtime()))
print(time.localtime().tm_year)
