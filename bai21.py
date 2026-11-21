n = int(input())

def km(a:int):
	money = 0
	if a >= 31:
		money = 12000 + 29*10000 + (a-30)*9000
	elif a>=2:
		money = 12000 + (a-1)*10000
	else:
		money = 12000
	return money

print(km(n))

