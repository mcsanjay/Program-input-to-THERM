f = open("H_repulsion.txt", 'w')

a = ["C1H3O0","C2H2O0","C1H2O1"]

for i in range(3):
	for j in a[i:]:
		for k in a:
			f.write("{}/{}\t{}\t1\n".format(a[i],j,k))
			
f.close()
