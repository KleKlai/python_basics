def intAdd(a,b):
	result = a+b
	print(result)
	

def intSub(a,b):
	result = a-b
	print(result) 

def intMultiply(a,b):
	result = a*b
	print(result)

def intDivide(a,b):
	result = a/b
	print(result)

def intFloor(a,b):
	result = a//b
	print(result)

def intExponent(a,b):
	result = a**b
	print(result)

def intModulo(a,b):
	result = a%b
	print(result)

def intList(a,b):
	result = list((a,b))
	print(result)

def intTuples(a,b):
	result = tuple((a,b))
	print(result)

def intSet(a,b):
	result = set((a,b))
	print(result)

def intDictionary(a,b):
	result = dict(number1= a,number2= b)
	print(result)

def intGreaterThan(a,b):
	if a> b:
		print(str(a)+" is greater than "+str(b))
	
	elif b > a:
		print(str(b)+" is greater than "+str(a))

def intLessThan(a,b):
	if a < b:
		print(str(a)+" is less than"+str(b))
	elif b < a:
		print(str(b)+" is less than"+str(a)) 

def intEqual(a,b):
	if(a == b):
		pint(str(a)+" and "+str(b)+" are equal")

	else:
		print("Both numbers are not equal")

def intFor(a,b):
	for x in range(3,5):
		print(x, end=" ")
	print()

def intWhile(a,b):
	while a <= b:
		print(a, end=" ")
		a+=1
	print()

def intRecursion(a,b):
	while a <= b:
		print(a, end=" ")
		a+=1
		return intRecursion(a,b)
	print()

def intReverse(a,b):
	while b >= a:
		print(b,end=" ")
		b-=1
	print()

def intMatrix(a,b):
	lineCount = 1
	for x in range(a):
		if lineCount != b:
			print(x+1,end=", ")
			lineCount+=1
		else:
			print(x+1,end=" ")
			print()
			lineCount=1
	print()

def intSkip(a,b,c):
	for x in range(a,b,c):
		print(x,end=", ")

intAdd(3,5)
intSub(3,5)
intMultiply(3,5)
intModulo(3,5)
intDivide(3,5)
intFloor(3,5)
intExponent(3,5)
intList(3,5)
intTuples(3,5)
intSet(3,5)
intDictionary(3,5)
intGreaterThan(3,5)
intLessThan(3,5)
intEqual(3,5)
intFor(3,5)
intWhile(3,7)
intRecursion(2,19)
intReverse(5,50	)
intMatrix(20,3)
intSkip(1,40,3)