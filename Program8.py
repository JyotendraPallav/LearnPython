# Program 8: Print n+nn+nnn

n=input("Please input a number: ")
n1=str(n)
n2=n1+str(n)
n3=n2+str(n)

print("The final result of %s+%s+%s is:%i" %(n1,n2,n3,int(n1)+int(n2)+int(n3)))