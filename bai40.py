n = int(input())

def isSoChinhPhuong(a:int):
	if a**0.5 == int(a**0.5):
		return True
	return False
count = 0
i = 0
while True:	
	if isSoChinhPhuong(i):
		print(i, end = ' ')
		count += 1
	if count == n:
		break
	i += 1