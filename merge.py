a=[]
n=input("Enter the length of the list")
for i in range(n):
    a.append(input("Enter the number"))
   
def mergesort(a):
    if(len(a)>1):
        
        mid=len(a)/2
        l=a[0:mid]
        r=a[mid:n]

        mergesort(l)
        mergesort(r)
        i=0
        j=0
        k=0
        while(i < len(l) and j < len(r)):
            if(l[i]<r[j]):
                a[k]=l[i]
                i=i+1
            else:
                a[k]=r[j]
                j=j+1
            k=k+1
        while(i < len(l)):
            a[k]=l[i]
            i=i+1
            k=k+1
        while(j < len(r)):
            a[k]=r[j]
            j=j+1
            k=k+1
                
            
mergesort(a)
for i in range(n):
    print a[i]
