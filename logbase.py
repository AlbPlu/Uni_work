import math

def log_base(a, base):
	if a <= 0:
		return ("undefined - only defined for positive numbers")
	elif (base <= 0) or (b == 1):
		return ("undefined - base is defined positive and not equal to 1")
	else:
		return math.log(a, base)

a = float(input("enter number: "))
base = float(input("enter base: "))
print (log_base(a, base))

