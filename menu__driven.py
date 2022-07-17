# program 2 menu driven program for calculater

def sum(a,b):
    print("sum is",a+b)
    return()
def sub(a,b):
    print("sum is",a-b)
    return()
def multi(a,b):
    print("sum is",a*b)
    return()
def div(a,b):
    print("sum is",a/b)
    return()
    
n=int(input("Enter (1 for +) (2 for -) (3 for *) (4 for /)"))
a=int(input("Enter First element"))
b=int(input("Enter Second element"))
if n==1:
    sum(a,b)
elif n==2:
    sub(a,b)
elif n==3:
    multi(a,b)
elif n==4:
    div(a,b)
else:
    print("Wrong output")

#armsrong number

n=int(input("enter n:"))
n1=n
sum=0

while(n>0):
    r=n%10
    sum=sum+(r*r*r)
    n=n//10

if(n1==sum):
    print("Armstrong number")
    
else:
    print("not Armstrong number")
    
