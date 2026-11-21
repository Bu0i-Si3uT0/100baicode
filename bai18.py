def isNhuan(b:int):
	if b%400 == 0 or (b%4==0 and not b%100 == 0):
		return True
	return False

a,b = map(int,input().split())


if a in (1,3,5,7,8,10,12):
		print(31)
elif a in (2,4,6,9,11):
		print(30)
else:
	if isNhuan(b):
		print(29)
	else:
		print(28)

