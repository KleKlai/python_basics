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
	set = set((1,2,3,4,5))
	set.add(value1)
	print(set)

def setGetLength(set):
	print(len(set))

def setRemoveItem(set,item):
	set.remove(item)
	print(set)

def 

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