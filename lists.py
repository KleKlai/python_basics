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
