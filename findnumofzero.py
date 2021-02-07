number = int(input("factorial number is : "))
nap = 0
count = 0
factorial = 1
if number < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,number + 1):
       factorial = factorial*i
       if i==number:
       	nap = factorial
       	list_string = map(str,str(nap))
       	#print(list(list_string))
       	for n in list_string:
       		if n == "0":
       			count = count + 1
       		else:
       			count = 0
       	print("count number zero is : ",count)
   print("The factorial of",str(number),"is",factorial)	