import re,string
print("The idea of this code is to read all phone numbers and save them accordingly into number and extension")
Phone_number =['800-555-1212','800 555 1212','800.555.1212','(800) 555-1212','1-800-555-1212','800-555-1212-1234','800-555-1212x1234','800-555-1212 ext. 1234','work 1-(800) 555.1212 #1234']
print(type(Phone_number),str(Phone_number[1]))
phonepattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})$')
for Pnumber in Phone_number:
    print(Pnumber,": ",phonepattern.search(Pnumber).groups())
