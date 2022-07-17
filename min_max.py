#min and max
n=int(input("Enter n: "))
list=[]
for i in range(1,n+1):
    r=int(input("Enter r: "))
    list.append(r)

max=list[0]
min=list[0]
for i in list:
    if(i>max):
        max=i
    if(i<min):
        min=i
        
print("max",max)
print("min",min)

#min and max

def min_max(list):
    max=list[0]
    min=list[0]
    for i in list:
        if(i>max):
            max=i
        if(i<min):
            min=i
        
    print("max",max)
    print("min",min)
    return()

n=int(input("Enter n: "))
list=[]
for i in range(1,n+1):
    r=int(input("Enter r: "))
    list.append(r)
min_max(list)
