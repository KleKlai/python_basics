def string_Upper(string):
	string = str(string).upper()
	print(string)

def string_Lower(string):
	string = str(string).lower()
	print(string)

def string_Length(string):
	print(len(string))

def string_Concat(string1,string2):
	print(str(string1)+", "+str(string2))

def string_Int_Str(num):
	num = str(num)
	print(num, end=" --> ")
	print(str(type(num)))

def string_Float_Str(num):
	num = str(num)
	print(num, end=" --> ")
	print(str(type(num)))

def string_Profanity(string,filters):
	if filters in string:
		string = string.replace(filters, "****")
		print(string)

def string_Display(string):
	print(str(string))

def string_Type_Int(int):
	print(str(type(int)))

def string_Type_Float(float):
	print(str(type(float)))

def string_Type_Str(string):
	print(str(type(string)))

def string_Type_Bool(bool):
	print(str(type(bool)))

def string_Type_List(list):
	print(str(type(list)))

def string_List(string):
	print(list((string[slice(0,len(string))])))

def string_Tuple(string):
	print(tuple((string[slice(0,len(string))])))

def string_Set(string):
	print(set((string[slice(0,len(string))])))

def string_List_String(list):
	for x in list:
		print(x,end="")
	print()

def string_Tuple_String(tuple):
	for x in tuple:
		print(x,end=" ")
	print()

def string_Loop(string):
	for x in string:
		print(x,end=" ")
	print()

def string_Remove(string,remove):
	if remove in string:
		string = string.replace(remove, "")
		print(string)

def string_Update(string,update,replace):
	if update in string:
		string = string.replace(update, replace)
		print(string)



string_Upper("Hello")
string_Lower("HELLO")
string_Length("Hello")
string_Concat("Hello","World")
string_Int_Str(int(456))
string_Float_Str(float(4.5))
string_Profanity(str("I wanna fuck"),str("fuck"))
string_Remove("I wanna fuck",str("fuck"))
string_Update("I wanna fuck",str("fuck"),str("hug"))
string_Display("Hello")
string_Type_Int(3)
string_Type_Float(4.5)
string_Type_Bool(True)
string_Type_List(list((1,2,3)))
string_List("Hello")
string_Tuple("Hello")
string_Set("Hello")
string_List_String(list(("H","E","L","L","O")))
string_Tuple_String(tuple(("W","O","R","L","D")))
string_Loop("Hello")



