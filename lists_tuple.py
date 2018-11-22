def list_Add(array,addTo):
	array = list(array)
	array.append(addTo)
	print(array)

def list_Remove(array,delete):
	array = list(array)
	array.remove(delete)
	print(array)

def list_Insert(array,insert,value):
	array = list(array)
	array.insert(2,value)
	print(array)

def list_Pop(array):
	array = list(array)
	array.pop()
	print(array)

def list_Loop(array):
	array =list(array)
	for x in array:
		print(x, end=" ")
	print()

def list_While(array):
	array = list(array)
	x=0
	while x < len(array):
		print(array[x], end=", ")
		x+=1
	print()	

def list_Int(array):
	for x in array:
		x = int(x)
		print(x,end=", ")
	print()

def list_Float(array):
	for x in array:
		x = float(x)
		print(x,end=", ")
	print()

def list_String(array):
	for x in array:
		x = str(x)
		print(x,end=", ")
	print()

def list_Bool(array):
	for x in array:
		if str(x) == "True" or str(x) == "False":
			print(x,end=" ")
		else:
			continue 
	print()

def tuple_Count(tuple,num):
	print(str(tuple.count(num)))


def tuple_Index(tuple,num):
	print(str(tuple.index(num)))

def tuple_Loop_Odd(tuple):
	for x in tuple:
		if x % 2 != 0:
			print(x, end=" ")
	print()

def tuple_Loop_Even(tuple):
	for x in tuple:
		if x % 2 == 0:
			print(x, end=" ")
	print()

def tuple_Find_Multiple(num):
	tuplenum = list()
	for x in range(1,5,1):
		num = num*x
		tuplenum.append(num)
	print(tuplenum)

def tuple_Find_String_Length(tuple, length):
	for x in tuple:
		if len(x) == length:
			print(x, end=" ")
	print()

def tuple_Add_Odd(tuple):
	result = 0
	for x in tuple:
		if x % 2 != 0:
			result+=x
	print(result)

def tuple_Add_Even(tuple):
	result = 0
	for x in tuple:
		if x % 2 == 0:
			result+=x
	print(result)

def tuple_Multiply_Odd(tuple):
	result = 1
	for x in tuple:
		if x % 2 != 0:
			result*=x
	print(result)

def tuple_Multiply_Even(tuple):
	result = 1
	for x in tuple:
		if x % 2 == 0:
			result*=x
	print(result)

def tuple_Dec_Binary(tuple):
	string = str()
	binary = str()
	for x in tuple:
		string+=str(x)
	num = int(string)
	while num > 1:
		num/=2
		if int(num) % 2 == 0:
			binary+=str(0)
		else:
			binary+=str(1)
	print(binary)

list_Add(list((1,4,8,12,16)),18)
list_Remove(list((1,4,8,12,16)),16)
list_Insert(list((1,2,3,4,5,6)),15,4)
list_Pop(list((4,5,6,7,8,9)))
list_Loop(list((1,2,3,4,5,6)))
list_While(list((1,2,3,4,5,6)))
list_Int(list((1.4,4.5,6)))
list_Float(list((2.5,1.5,2,4)))
list_String(list(("Hi", 5,"Hello","World")))
list_Bool(list((True, "Yeaahh",False)))
tuple_Count(tuple((1,1,1,2,3,4,4,5)),1)
tuple_Index(tuple((1,2,3,4,5)),5)
tuple_Loop_Odd(tuple((1,2,3,4,5,6,7)))
tuple_Loop_Even(tuple((1,2,3,4,5,6,7)))
tuple_Find_String_Length(tuple(("Hello","Hi","My name is","Pi")),2)
tuple_Add_Odd(tuple((1,2,3,4,5,6,7)))
tuple_Add_Even(tuple((1,2,3,4,5,6,7)))
tuple_Multiply_Odd(tuple((1,2,3,4,5,6,7)))
tuple_Multiply_Even(tuple((1,2,3,4,5,6,7)))
tuple_Dec_Binary(tuple((5,6,7)))


