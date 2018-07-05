z = int(input("boyutunu yazın: "))
for x in range(1,z+1):
	for y in range(1,z+1):
		if (x+y==z+1):
			print(1,end="\t")
		if (x+y!=z+1):
			print(0,end="\t")
	print("\n")
