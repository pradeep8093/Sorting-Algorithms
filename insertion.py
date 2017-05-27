a=[]
n=input("Enter the length of the list")
for i in range(n):
    a.append(input("Enter the number"))
   

for j in range(1,n):
    key=a[j]
    k=j-1;
    while(k>=0 and a[k]>key):
        a[k+1]= a[k]
        k=k-1
    a[k+1]=key

for i in range(0,n):
    print a[i]
