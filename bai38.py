n = int(input())

def isNguyenTo(a:int):
	count = 0
	for i in range(1,a+1):
		if a%i == 0:
			count += 1
	if count > 2:
		return False
	return True
count = 0
i = 1
while True:
	i+= 1
	if isNguyenTo(i):
		count += 1
		print(i, end = ' ')
	if count == n:
		break