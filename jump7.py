a=1
for a in range(101):
	if a%7==0:
		continue
	elif a%10==7:
		continue
	elif a//10==7:
		continue
	else:
		print(a)
