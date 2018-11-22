def int_Add(a,b):
	result = a+b
	return result
	

def int_Sub(a,b):
	result = a-b
	return result

def int_Multiply(a,b):
	result = a*b
	return result

def int_Divide(a,b):
	result = a/b
	return result

def int_Floor(a,b):
	result = a//b
	return result

def int_Exponent(a,b):
	result = a**b
	return result

def int_Modulo(a,b):
	result = a%b
	return result

def int_List(a,b):
	result = list((a,b))
	return result

def int_Tuples(a,b):
	result = tuple((a,b))
	return result

def int_Set(a,b):
	result = set((a,b))
	return result

def int_Dictionary(a,b):
	result = dict(number1= a,number2= b)
	return result

def int_Greater_Than(a,b):
	if a> b:
		return str(str(a)+" is greater than "+str(b))
	
	elif b > a:
		return str(str(b)+" is greater than "+str(a))

def int_Less_Than(a,b):
	if a < b:
		return str(str(a)+" is less than"+str(b))
	elif b < a:
		return str(str(b)+" is less than"+str(a)) 

def int_Equal(a,b):
	if(a == b):
		return str(str(a)+" and "+str(b)+" are equal")

	else:
		return str("Both numbers are not equal")

def int_For(a,b):
	for x in range(3,5):
		print(x, end=" ")
	print()

def int_While(a,b):
	while a <= b:
		return a
		a+=1
	print()

def int_Recursion(a,b):
	while a <= b:
		return a
		a+=1
		return int_Recursion(a,b)
	

def int_Reverse(a,b):
	while b >= a:
		print(b,end=" ")
		b-=1
	print()

def int_Matrix(a,b):
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

def int_Skip(a,b,c):
	for x in range(a,b,c):
		print(x,end=", ")

print(int_Add(3,5))
print(int_Sub(3,5))
print(int_Multiply(3,5))
print(int_Modulo(3,5))
print(int_Divide(3,5))
print(int_Floor(3,5))
print(int_Exponent(3,5))
print(int_List(3,5))
print(int_Tuples(3,5))
print(int_Set(3,5))
print(int_Dictionary(3,5))
print(int_Greater_Than(3,5))
print(int_Less_Than(3,5))
print(int_Equal(3,5))
int_For(3,5)
int_While(3,7)
print(int_Recursion(2,19))
int_Reverse(5,50	)
int_Matrix(20,3)
int_Skip(1,40,3)