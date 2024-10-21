def exp(base, a):
	if (base == 0) and (a == 0):
		return ("0^0 is inderminate")
	else:
		return base ** a

base = float(input("enter base value: "))
a = flaot(input("enter exponent value: "))
print (exp(base,a))
