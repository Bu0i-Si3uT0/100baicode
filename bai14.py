t = int(input())

if 0 < t <= 150:
	if 0 < t <= 11:
		print('Thieu nhi')
	elif 11 < t <= 25:
		print("Thieu nien")
	elif 25 < t <= 50:
		print("Trung nien")
	else:
		print("Lao nien")
