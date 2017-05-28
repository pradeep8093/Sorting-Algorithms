a=[]
n=input("Enter the length of the list")
for i in range(n):
    a.append(input("Enter the number"))

def partition(a,low,high):
    i=low-1
    p=a[high]

    for j in range(low,high):
        if(a[j]<=p):
            i=i+1
            a[j],a[i]=a[i],a[j]
    a[i+1],a[high]=a[high],a[i+1]
    return(i+1)
        


def quicksort(a,low,high):
    if(low<high):
        pi=partition(a,low,high)
        
        quicksort(a,low,pi-1)
        quicksort(a,pi+1,high)

quicksort(a,0,n-1)
for i in range(0,n):
    print a[i]
