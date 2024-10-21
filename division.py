def division(a ,b):
	if b == 0:
		return("Cannot divide by 0")
	else:
		return (a/b)

a = float(input("enter first number: "))
b = float(input("enter second number: "))
print(division(a,b))

