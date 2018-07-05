z = int(input("boyutunu yazın: "))
for x in range(1,z+1):
	for y in range(1,z+1):
		print(y*x,end="\t")
	print("\n")
