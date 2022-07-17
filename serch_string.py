#serch string in the list

def pass_list():
    for t in list:
        if r in t:
            print("Yes found string")
        else:
            print("Not found string")
    return()

n=int(input("Enter n: "))
list=[]
for i in range(1,n+1):
   m=input("Enter string: ")
   list.append(m)
print(list)
r=input("Enter serch string: ")

pass_list()


#serch caracter in the string
def pass_list(str):
    for i in str:
        c=0
        for j in i:
            if j==r:
                c=c+1
        print(i," ",c)
            
s=input("enter string")
str=s.split()
print(str)
r=input("Enter serch character")
pass_list(str)


#check given string is palindrom or not


s=input("enter string: ")
s1=s[::-1]

if(s1==s):
    print("palindrom")
else:
    print("Not palindrom")


      
   
#program pass string as list to udf and display string in reverse order
def pass_list():
    for i in spl:
        rev=spl[::-1]
        print(rev)
        return()
n=input("enter string: ")
spl=n.split()
print(spl)
pass_list()





