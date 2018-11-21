def listAdd(array,addTo):
	array = list(array)
	array.append(addTo)
	print(array)

def listRemove(array,delete):
	array = list(array)
	array.remove(delete)
	print(array)

def listInsert(array,insert,value):
	array = list(array)
	array.insert(2,value)
	print(array)

def listPop(array):
	array = list(array)
	array.pop()
	print(array)

def listLoop(array):
	array =list(array)
	for x in array:
		print(x, end=" ")
	print()

def listWhile(array):
	array = list(array)
	x=0
	while x < len(array):
		print(array[x], end=", ")
		x+=1
	print()	

def listInt(array):
	for x in array:
		x = int(x)
		print(x,end=", ")
	print()

def listFloat(array):
	for x in array:
		x = float(x)
		print(x,end=", ")
	print()

def listString(array):
	for x in array:
		x = str(x)
		print(x,end=", ")
	print()

def listBool(array):
	for x in array:
		if str(x) == "True" or str(x) == "False":
			print(x,end=" ")
		else:
			continue 
	print()

def tupleCount(tuple,num):
	print(str(tuple.count(num)))


def tupleIndex(tuple,num):
	print(str(tuple.index(num)))

def tupleLoopOdd(tuple):
	for x in tuple:
		if x % 2 != 0:
			print(x, end=" ")
	print()

def tupleLoopEven(tuple):
	for x in tuple:
		if x % 2 == 0:
			print(x, end=" ")
	print()

def tupleFindMultiple(num):
	tuplenum = list()
	for x in range(1,5,1):
		num = num*x
		tuplenum.append(num)
	print(tuplenum)

def tupleFindStringLength(tuple, length):
	for x in tuple:
		if len(x) == length:
			print(x, end=" ")
	print()

def tupleAddOdd(tuple):
	result = 0
	for x in tuple:
		if x % 2 != 0:
			result+=x
	print(result)

def tupleAddEven(tuple):
	result = 0
	for x in tuple:
		if x % 2 == 0:
			result+=x
	print(result)

def tupleMultiplyOdd(tuple):
	result = 1
	for x in tuple:
		if x % 2 != 0:
			result*=x
	print(result)

def tupleMultiplyEven(tuple):
	result = 1
	for x in tuple:
		if x % 2 == 0:
			result*=x
	print(result)

def tupleDecBinary(tuple):
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

listAdd(list((1,4,8,12,16)),18)
listRemove(list((1,4,8,12,16)),16)
listInsert(list((1,2,3,4,5,6)),15,4)
listPop(list((4,5,6,7,8,9)))
listLoop(list((1,2,3,4,5,6)))
listWhile(list((1,2,3,4,5,6)))
listInt(list((1.4,4.5,6)))
listFloat(list((2.5,1.5,2,4)))
listString(list(("Hi", 5,"Hello","World")))
listBool(list((True, "Yeaahh",False)))
tupleCount(tuple((1,1,1,2,3,4,4,5)),1)
tupleIndex(tuple((1,2,3,4,5)),5)
tupleLoopOdd(tuple((1,2,3,4,5,6,7)))
tupleLoopEven(tuple((1,2,3,4,5,6,7)))
tupleFindStringLength(tuple(("Hello","Hi","My name is","Pi")),2)
tupleAddOdd(tuple((1,2,3,4,5,6,7)))
tupleAddEven(tuple((1,2,3,4,5,6,7)))
tupleMultiplyOdd(tuple((1,2,3,4,5,6,7)))
tupleMultiplyEven(tuple((1,2,3,4,5,6,7)))
tupleDecBinary(tuple((5,6,7)))


