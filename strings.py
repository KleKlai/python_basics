def string_Upper(string):
	string = str(string).upper()
	return string

def string_Lower(string):
	string = str(string).lower()
	return string

def string_Length(string):
	return len(string)

def string_Concat(string1,string2):
	return str(string1)+", "+str(string2)

def string_Int_Str(num):
	num = str(num)
	return num
	

def string_Float_Str(num):
	num = str(num)
	return str(type(num))

def string_Profanity(string,filters):
	if filters in string:
		string = string.replace(filters, "****")
	return str(string)

def string_Display(string):
	return str(string)

def string_Type_Int(int):
	return str(type(int))

def string_Type_Float(float):
	return str(type(float))

def string_Type_Str(string):
	return str(type(string))

def string_Type_Bool(bool):
	return str(type(bool))

def string_Type_List(list):
	return str(type(list))

def string_List(string):
	return list((string[slice(0,len(string))]))

def string_Tuple(string):
	return tuple((string[slice(0,len(string))]))

def string_Set(string):
	return set((string[slice(0,len(string))]))

def string_List_String(list):
	string = str()
	for x in list:
		string+=x
	return string

def string_Tuple_String(tuple):
	string = str()
	for x in tuple:
		string+=x
	return string

def string_Loop(string):
	string = str()
	for x in string:
		string+=x
	return string
def string_Remove(string,remove):
	if remove in string:
		string = string.replace(remove, "")
	return str(string)

def string_Update(string,update,replace):
	if update in string:
		string = string.replace(update, replace)
	return str(string)


print(string_Upper("Hello"))
print(string_Lower("HELLO"))
print(string_Length("Hello"))
print(string_Concat("Hello","World"))
print(string_Int_Str(int(456)))
print(string_Float_Str(float(4.5)))
print(string_Profanity(str("I wanna fuck"),str("fuck")))
print(string_Remove("I wanna fuck",str("fuck")))
print(string_Update("I wanna fuck",str("fuck"),str("hug")))
print(string_Display("Hello"))
print(string_Type_Int(3))
print(string_Type_Float(4.5))
print(string_Type_Bool(True))
print(string_Type_List(list((1,2,3))))
print(string_List("Hello"))
print(string_Tuple("Hello"))
print(string_Set("Hello"))
print(string_List_String(list(("H","E","L","L","O"))))
print(string_Tuple_String(tuple(("W","O","R","L","D"))))
print(string_Loop("Hello"))



