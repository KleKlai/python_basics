import math

def float_Add(a,b):
	result = float(a)+float(b)
	print(result)

def float_Sub(a,b):
	result = float(a) - float(b)
	print(result)

def float_Divide(a,b):
	result = float(a) / float(b)
	print(result)

def float_Mult(a,b):
	result = float(a) * float(b)
	print(result)

def float_Floor(a,b):
	result = float(a) // float(b)
	print(result)

def float_Exponent(a,b):
	result = float(a) ** float(b)
	print(result)

def float_Modulo(a,b):
	result = float(a) % float(b)
	print(result)

def float_Speed(a,b,c):
	for x in range(a,b,c):
		print(str(x)+" mph")

def float_Pay(money,price):
	if float(money) >= float(price):
		change = float(money) - float(price)
		print("Product Bought!")
		print("Change: PHP %.2f" %change)
	else:
		print("Isufficient funds")

def float_Money_Convert(peso,countryAvailable):
	if str(countryAvailable.upper()) == "USA":
		money = peso * 0.019
		print("PHP -> USA = $ "+str(float(money)))

	elif str(countryAvailable.upper()) == "JAPAN":
		money = peso * 2.14
		print("PHP -> JAPAN = YEN "+str(float(money)))

def float_Verify(array):
	for x in array:
		if str(type(x)) == "<class 'float'>":
			print(str(x)+" is a float")

def float_To_Int(a):
	print(int(a))

def float_Ave_Height(maxHeight):
	aveHeight = (float(maxHeight)/2)
	print(str(aveHeight)+" ft")

def float_Diameter(radius):
	diameter = 2 * radius
	print("%.2f" %diameter)

def float_Diam_Circum(circumeference):
	diameter = circumeference/ math.pi
	print("%.2f" %diameter)

def float_Diam_Area(area):
	diameter = math.sqrt(area/math.pi) * 2
	print("%.2f" %diameter)

def float_Area_Triangle(base,height):
	area = 1/2 *(float(base) * float(height))
	print("%.2f" %area)

def float_Height_Triangle(area,base):
	height = (area/base) * 2
	print("%.2f" %height)

def float_Area_Parallelogram(base,height):
	area = base * height
	print("%.2f" %area)

def float_Height_Parallelogram(area,base):
	height = area/base
	print("%.2f" %height)

float_Add(5.3,6.5)
float_Sub(5.3,6.2)
float_Divide(4.6,10.2)
float_Mult(3.5,5.5)
float_Floor(2.5,6.5)
float_Exponent(4.5,2)
float_Modulo(2.5,6.8)
float_Speed(1,60,2)
float_Pay(1000,790)
float_Money_Convert(2000,"Japan")
float_Verify([1,1.5,2,2.67])
float_To_Int(4.567)
float_Ave_Height(7.5)
float_Diameter(5.56)
float_Diam_Circum(6.96)
float_Diam_Area(4.68)
float_Area_Triangle(5.6,6.8)
float_Height_Triangle(4.5,3.5)
float_Area_Parallelogram(7.6,8.5)
float_Height_Parallelogram(10.5,5.5)