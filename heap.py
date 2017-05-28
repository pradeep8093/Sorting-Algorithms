a=[]
n=input("Enter the length of the list")
for i in range(n):
    a.append(input("Enter the number"))

def heapify(a,n,i):
    l=2*i + 1
    r=2*i + 2
    largest = i
    if(l<n and a[largest]<a[l]):
        largest=l
    if(r<n and a[largest]<a[r]):
        largest=r
    if(largest!=i):
        a[i],a[largest]=a[largest],a[i]
        heapify(a,n,largest)


def heapsort(a,n):
    for i in range(n-1,-1,-1):
        heapify(a,n,i)

    for i in range(n-1,-1,-1):
        a[i],a[0]=a[0],a[i]
        heapify(a,i,0)

heapsort(a,n)
for i in range(0,n):
    print a[i]
