a=[]
n=input("Enter the length of the list")
for i in range(n):
    a.append(input("Enter the number"))
   
switch=True
if(switch==True):
	for i in range(0,n):
		switch=False
		for j in range(0,n-i-1):
			if(a[j]>a[j+1]):
				switch=True
				a[j],a[j+1]=a[j+1],a[j]

for i in range(0,n):
    print a[i]
