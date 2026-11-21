money = int(input())
a=b=c=0

def oke(n:int):
	if n%1000==0 and n <= 1000000:
		return True
	return False

if oke(money):
	while money > 0:
		a = money//5000
		money -= a*5000
		b = (money)//2000
		money -= b*2000
		c = (money)//1000
		money -= c*1000
print(a,b,c)
