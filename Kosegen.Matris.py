z = int(input("boyutunu yazın: "))
for x in range(z):
	for y in range(z):
		if (x==y):
			print(1,end="\t")
		if (x!=y):
			print(0,end="\t")
	print("\n")
