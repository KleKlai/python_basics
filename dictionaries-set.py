def dictAddValues(dict):
	result = 0
	for x in dict.values():
		result += x
	print(result)

def dictSubValues(dict):
	result = max(dict.values())
	for x in dict.values():
		result -= x
	print(result)


def dictMultiplValues(dict):
	result = 1
	for x in dict.values():
		result *= x
	print(result)

def dictDivideValues(dict):
	result = 1
	for x in dict.values():
		result /= x
	print(result)

def dictSearch(dict,search):
	if search in dict:
		print(str(dict[search])+" is present")

def dictAdd(dict,key,value):
	dict[key] = value
	print(dict)

def dictUpdate(dict,key,value):
	dict[key] = value
	print(dict)

def dictRemove(dict,key):
	dict.pop(key)
	print(dict)

def dictAssign(list1,list2):
	dictionary = dict() 

	for x in range(len(list1)):
		for y in range(len(list2)):
			dictionary[list1[x]] = list2[y]
			list2.pop(y)
			break

	print(dictionary)

def dictConcatValue(dictionary,key1,key2):
	key1 = dictionary[key1]
	key2 = dictionary[key2]
	print(str(key1)+" "+str(key2))

def setAddItem(value1):
	sets = set((1,2,3,4,5))
	sets.add(value1)
	print(sets)

def setGetLength(set):
	print(len(set))

def setRemoveItem(set,item):
	set.remove(item)
	print(set)

def setAssignToDict(set,item,value):
	dictionary = dict()
	if item in set:
		dictionary[item] = value
	print(dictionary)

def setAssignToListofDict(set,item,value):
	lists = list(())
	dictionary = dict()
	if item in set:
		dictionary[item] = value
		lists.append(dictionary)
	print(lists)

def setAssignToTuple(set,item,value):
	dictionary = dict()
	if item in set:
		dictionary[item] = value
		tuples = tuple((dictionary,1))
	print(tuples)

def setLength(set):
	print(len(set))

def setMaxValue(set):
	print(max(set))

def setIdentifyType(set,item):
	if item in set:
		print(str(item)+" is "+str(type(item)))
	else:
		print("Item not Found")

def setUpdateItems(set,item):
	set.update([item])
	print(set)
	


dictAddValues(dict(a=1,b=2))
dictSubValues(dict(a=4,b=5))
dictMultiplValues(dict(a=1,b=8))
dictDivideValues(dict(a=10,b=11))
dictSearch(dict(a=1,b=2),"a")
dictAdd(dict(a=10,b=11),"c",12)
dictUpdate(dict(a=10,b=11),"a",9)
dictRemove(dict(a=10,b=11,c=12),"c")
dictAssign(list(("Miguel","Ghelo")),list((1,2)))
dictConcatValue(dict(firstname="Miguel",lastname="Dorado"),"firstname","lastname")
setAddItem(6)
setGetLength(set((1,2,3,4,5)))
setRemoveItem(set((1,23,4,5,6,)),23)
setAssignToDict(set(("Banana","Apple","Carrot")),"Banana",1000)
setAssignToListofDict(set(("Banana","Apple","Carrot")),"Banana",1000)
setAssignToTuple(set(("Banana","Apple","Carrot")),"Banana",1000)
setLength(set(("Banana","Apple","Carrot")))
setMaxValue(set(("Banana","Apple","Carrot")))
setIdentifyType(set(("Banana","Apple","Carrot",1,1.5,True)),True)
setUpdateItems(set(("Banana","Apple","Carrot",1,1.5,True)),"Pineapple")