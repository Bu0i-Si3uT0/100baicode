n = int(input())

def w(a:int):
	money = 0
	if a >= 201:
		money = 50*600 + 50*800 + 100*1100 + (a-200)*1500
	elif a>=101:
		money = 50*600 + 50*800 + (a-100)*1100
	elif a>= 51:
		money = 50*600 + (a-50)*800
	else:
		money = a*600
	return money

print(w(n))
