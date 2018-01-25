# Program 10 - Find difference between two dates

First_Date=(2017,1,1)
Second_Date=(2015,12,31)
# (First_Date,Second_Date)=input("Please enter both dates (YYYY,MM,DD),(YYYY,MM,DD): ")
Num_Days = (First_Date[0]-Second_Date[0])*365 + (First_Date[1]-Second_Date[1])*30 + (First_Date[2]-Second_Date[2])
       
print ("Days between dates using poor logic: ",Num_Days)

from datetime import date
F_Date=date(2017,1,1)
S_Date=date(2015,12,31)
print ("Days between dates using Package datetime:", (F_Date-S_Date).days)