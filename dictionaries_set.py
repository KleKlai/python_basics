def dict_Add_Values(dict):
	result = 0
	for x in dict.values():
		result += x
	print(result)

def dict_Sub_Values(dict):
	result = max(dict.values())
	for x in dict.values():
		result -= x
	print(result)


def dict_Multiply_Values(dict):
	result = 1
	for x in dict.values():
		result *= x
	print(result)

def dict_Divide_Values(dict):
	result = 1
	for x in dict.values():
		result /= x
	print(result)

def dict_Search(dict,search):
	if search in dict:
		print(str(dict[search])+" is present")

def dict_Add(dict,key,value):
	dict[key] = value
	print(dict)

def dict_Update(dict,key,value):
	dict[key] = value
	print(dict)

def dict_Remove(dict,key):
	dict.pop(key)
	print(dict)

def dict_Assign(list1,list2):
	dictionary = dict() 

	for x in range(len(list1)):
		for y in range(len(list2)):
			dictionary[list1[x]] = list2[y]
			list2.pop(y)
			break

	print(dictionary)

def dict_Concat_Value(dictionary,key1,key2):
	key1 = dictionary[key1]
	key2 = dictionary[key2]
	print(str(key1)+" "+str(key2))

def set_Add_Item(value1):
	sets = set((1,2,3,4,5))
	sets.add(value1)
	print(sets)

def set_Get_Length(set):
	print(len(set))

def set_Remove_Item(set,item):
	set.remove(item)
	print(set)

def set_Assign_To_Dict(set,item,value):
	dictionary = dict()
	if item in set:
		dictionary[item] = value
	print(dictionary)

def set_Assign_To_List_of_Dict(set,item,value):
	lists = list(())
	dictionary = dict()
	if item in set:
		dictionary[item] = value
		lists.append(dictionary)
	print(lists)

def set_Assign_To_Tuple(set,item,value):
	dictionary = dict()
	if item in set:
		dictionary[item] = value
		tuples = tuple((dictionary,1))
	print(tuples)

def set_Length(set):
	print(len(set))

def set_Max_Value(set):
	print(max(set))

def set_Identify_Type(set,item):
	if item in set:
		print(str(item)+" is "+str(type(item)))
	else:
		print("Item not Found")

def set_Update_Items(set,item):
	set.update([item])
	print(set)
	


dict_Add_Values(dict(a=1,b=2))
dict_Sub_Values(dict(a=4,b=5))
dict_Multiply_Values(dict(a=1,b=8))
dict_Divide_Values(dict(a=10,b=11))
dict_Search(dict(a=1,b=2),"a")
dict_Add(dict(a=10,b=11),"c",12)
dict_Update(dict(a=10,b=11),"a",9)
dict_Remove(dict(a=10,b=11,c=12),"c")
dict_Assign(list(("Miguel","Ghelo")),list((1,2)))
dict_Concat_Value(dict(firstname="Miguel",lastname="Dorado"),"firstname","lastname")
set_Add_Item(6)
set_Get_Length(set((1,2,3,4,5)))
set_Remove_Item(set((1,23,4,5,6,)),23)
set_Assign_To_Dict(set(("Banana","Apple","Carrot")),"Banana",1000)
set_Assign_To_List_of_Dict(set(("Banana","Apple","Carrot")),"Banana",1000)
set_Assign_To_Tuple(set(("Banana","Apple","Carrot")),"Banana",1000)
set_Length(set(("Banana","Apple","Carrot")))
set_Max_Value(set(("Banana","Apple","Carrot")))
set_Identify_Type(set(("Banana","Apple","Carrot",1,1.5,True)),True)
set_Update_Items(set(("Banana","Apple","Carrot",1,1.5,True)),"Pineapple")