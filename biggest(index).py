#ใส่ค่าเอง
lis = []
n = int(input("Enter your length of number : "))
for i in range(0,n):
	ele = int(input("input number "+str(i+1)+" :"))
	lis.append(ele)

biggest = [0]
for i in range(len(lis)-1):
	for j in range(len(lis)-i-1):
		if(lis[j]>lis[j+1]):
			lis[j+1],lis[j] = lis[j],lis[j+1]
print("biggest number in index is : ",lis[-1])

''' กำหนดค่าให้เลย
x = [1,20,1,3,9,6,4]
biggest = [0]
for i in range(len(x)-1):
	for j in range(len(x)-i-1):
		if(x[j]>x[j+1]):
			x[j+1],x[j] = x[j],x[j+1]
print("biggest number is a index: ",x[j-1])
'''


