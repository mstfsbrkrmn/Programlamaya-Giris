a,b,c,d = [],[],[],[]

for y in range(0,100):
	for x in range(1,100):
		if (x%15==0):
			a.append(x)

for y in range(0,100):
	for x in range(1,31):
		if (x%5==0):
			b.append(x)

for y in range(0,100):
	for x in range(101,49,-1):
		if (x%10==0):
			c.append(x)

for y in range(0,100):
	for x in range(1,100):
		if (2**x<65):
			d.append(2**x)

for z in range(0,6):
	print(a[z:z+1],b[z:z+1],c[z:z+1],d[z:z+1],"\n")
