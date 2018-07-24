n=int(input("enter the number"))
k=int(input("enter the number"))
d=[]
sum=0
for i in range(0,n):
     p=int(input("enter the number"))
     d.append(p)
for j in range(0,k):
    sum=sum+d[j]
print (sum)