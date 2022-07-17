#program 1
""" A
   B C
  D E F"""
n=int(input("Enter n: "))
k=65

for i in range(1,n+1):
    for j in range(1,i):
        print(chr(k),end=" ")
        k=k+1
    print("\n")

#===============================================================    
n=int(input("enter n: "))
i=0
k=65

while(i<=n):
    j=0
    while(j<=i):
        print(chr(k),end=" ")
        k=k+1
        j=j+1
    print("\n")
    i=i+1
#===============================================================
#program 2
""" A
   A B
  A B C"""
n=int(input("Enter n: "))


for i in range(1,n+1):
    k=65
    for j in range(1,i):
        print(chr(k),end=" ")
        k=k+1
    print("\n")    
#===============================================================
    #program 2
""" a
   b c
  d e f"""
n=int(input("enter n: "))
i=0
k=97

while(i<=n):
    j=0
    while(j<=i):
        print(chr(k),end=" ")
        k=k+1
        j=j+1
    print("\n")
    i=i+1
#===============================================================
    #program 2
""" a
   a b
  a b c"""
n=int(input("enter n: "))
i=0


while(i<=n):
    k=97
    j=0
    while(j<=i):
        print(chr(k),end=" ")
        k=k+1
        j=j+1
    print("\n")
    i=i+1
