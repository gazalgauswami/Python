#fibbonacci series with while loop

n=int(input("Enter n: "))
a=0
b=1
i=0
c=0

print(a)
print(b)
while(i<=n-2):
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1

#fibbonacci series with for loop


n=int(input("Enter n: "))
a=0
b=1
c=0

print(a)
print(b)
for i in range(2,n+1):
    c=a+b
    print(c)
    a=b
    b=c
#1)fibbonacci series with function

def fibo():     
    n=int(input("Enter n: "))
    a=0
    b=1
    i=0
    c=0

    print(a)
    print(b)
    while(i<=n-2):
        c=a+b
        print(c)
        a=b
        b=c
        i=i+1
    return()
fibo()

#2)fibbonacci series with function

def fibo(n,a,b,i,c):     
    while(i<=n-2):
        c=a+b
        print(c)
        a=b
        b=c
        i=i+1
    return()
n=int(input("Enter n: "))
a=0
b=1
i=0
c=0
print(a)
print(b)
fibo(n,a,b,i,c)

   


