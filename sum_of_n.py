#sum of the n number by udf
#no argument no return

def sum():
    n=int(input("Enter n: "))
    i=0
    s=0
    while(i<=n):
        i=i+1
        s=s+i
        print(i,end=" ")
    print("sum is: ",s)
    return()
sum()

#argument but no return
def sum(n,s,i):
     while(i<=n):
        i=i+1
        s=s+i
        print(i,end=" ")
     print("sum is: ",s)
     return()
n=int(input("Enter n: "))
i=0
s=0
sum(n,s,i)

#no argument but return

def sum():
    n=int(input("Enter n: "))
    i=0
    s=0
    while(i<=n):
        i=i+1
        s=s+i
        print(i,end=" ")
    return(s)
print("sum is : ",sum())

#argument with return

def sum(i,n,s):
    while(i<=n):
        i=i+1
        s=s+i
        print(i,end=" ")
    return(s)
n=int(input("Enter n: "))
i=0
s=0
print("Sum is: ",sum(i,n,s))

#with simplale code
n=int(input("Enter n: "))
i=0
s=0
while(i<=n):
        i=i+1
        s=s+i
        print(i,end=" ")
print("Sum is: ",s)

#with for loop
n=int(input("Enter n: "))
i=0
s=0
for i in range(1,n+1):
    s=s+i
    print(i,end=" ")
print("sum is: ",s)

