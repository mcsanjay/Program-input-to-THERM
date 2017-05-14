


import all_classes


def string_atoms (bonds, atoms, na):
	a_str = []
	for i in range(na):
		nc = 0
		ncd = 0
		nct = 0
		no = 0
		nh = 0
		nod = 0
		for j in range(na):
			if (bonds[i][j] == 1):
				if (atoms[j+1] == 'C'):
					nc = nc + 1
				elif (atoms[j+1] == 'H'):
					nh = nh + 1
				elif (atoms[j+1] == 'O'):
					no = no + 1
			elif (bonds[i][j] == 2):
				if (atoms[j+1] == 'C'):
					ncd = ncd + 1
				elif (atoms[j+1] == 'O'):
					nod = nod + 1
			elif (bonds[i][j] == 3):
				if (atoms[j+1] == 'C'):
					nct = nct + 1
		
		a_str.append("C{}CD{}CT{}H{}O{}OD{}".format(nc,ncd,nct,nh,no,nod))
	
	return (a_str)
	
'''
def similar_groups (neigh_atoms_str):
	eql_grps = []	
	temp = []
	for i in range(len(neigh_atoms_str)):
		flag = 0
		for j in range(i+1,len(neigh_atoms_str)):
			if neigh_atoms_str[j] not in temp: 
				if (neigh_atoms_str[i] == neigh_atoms_str[j]):
					flag = 1
					eql_grps.append((i,j))
		if (flag == 1):
			temp.append(neigh_atoms_str[i])
	return (eql_grps)
'''

def similar_groups (neigh_atoms_str):
	eql_grps = []	
	#temp = []
	for i in range(len(neigh_atoms_str)):
		flag = 0
		for j in range(i+1,len(neigh_atoms_str)):
			#if neigh_atoms_str[j] not in temp: 
			if (neigh_atoms_str[i] == neigh_atoms_str[j]):
				flag = 1
				eql_grps.append((i,j))
		#if (flag == 1):
		#	temp.append(neigh_atoms_str[i])
	return (eql_grps)

'''
def create_graph (str_class_arr,root_no,parent_no):
	gr = []
	gr.append([])
	gr[0].append([])
	gr[0][0].append(str_class_arr[root_no])
	curr = root_no
	while (True):
		if (len(str_class_arr[curr].neighbours) > 1):
			gr.append([])
	for i in gr:
		for j in i:
			for k in j:
				


def compare_two_nodes (ac,bc,atom_str):			# ac,bc start from 0
	eql = 0
	eql_grps = []
	a = []
	b = []
	for i in ac:
		a.append(atom_str[i])
	for i in bc:
		b.append(atom_str[i])
	if (len(a) != len(b)):
		return (eql,eql_grps)
	else:
		a_and_b = set(a) & set(b)
		if ((len(set(a)) == len(a_and_b)) and (len(set(b)) == len(a_and_b))):
			flag = 0
			for i in a_and_b:
				if (a.count(i) != b.count(i)):
					flag = 1
					break
			if (flag == 1):
				return (eql,eql_grps)
			else:
				eql = 1
				if (len(a) == len(set(a))):
					temp = []
					for i in a:
						x = b.index(i)
						y = a.index(i)
						temp.append((ac[y],bc[x]))
					eql_grps.append(temp)
				if (len(a) == (len(set(a)) + 1)):
					temp = []
					for i in a:
						if (a.count(i) == 1):
							qa = a.index(i)
							qb = b.index(i)
					
					wa = []
					wb = []		
					for i in range(len(a)):
						if (i == qa):
							continue
						wa.append(i)
					for i in range(len(b)):
						if (i == qb):
							continue
						wb.append(i)
					
					if (len(wa) == 1)#############	
					eql_grps.append([(ac[wa[0]],bc[wb[0]]),(ac[wa[1]],bc[wb[1]]),(ac[qa],bc[qb])])
					eql_grps.append([(ac[wa[0]],bc[wb[1]]),(ac[wa[1]],bc[wb[0]]),(ac[qa],bc[qb])])
					
				if (len(a) == (len(set(a)) + 2)):
					
'''						
				


def create_string_class (bonds,atoms,atom_str,na):
	str_class_arr = []
	for i in range(na):
		temp = all_classes.atom_string()
		temp.number = i						# starting from 0
		temp.symbol = atoms[i+1]
		temp.string = atom_str[i]
		str_class_arr.append(temp)
	for i in str_class_arr:
		for j in range(na):
			if (bonds[i.number][j] > 0):
				i.neighbours.append(str_class_arr[j]) 
	return (str_class_arr)


def opt_isomer (c_atoms,bonds,atoms,na):
	atom_str = string_atoms(bonds,atoms,na)
	str_class_arr = create_string_class(bonds,atoms,atom_str,na)
	oi = 0	
				
	for i in str_class_arr:
		if (i.symbol == 'C'):
			if (len(i.neighbours) == 4):
				neigh_atoms_str = []
				for j in i.neighbours:
					neigh_atoms_str.append(j.string)
				if (neigh_atoms_str.count("C1CD0CT0H0O0OD0") > 1):
					continue
				
				#print(neigh_atoms_str)
				eql_grps = similar_groups(neigh_atoms_str)
				if (eql_grps == []):
					oi = oi + 1
					continue
				
				flag_count = 0
				for j in eql_grps:
					temp = []
					for k in j:
						temp.append(i.neighbours[k])
					for k in temp:
						k.create_children(i.number)
					
					flag = temp[0].compare_subgraph(temp[1])
					
					flag_count = flag_count + flag
					
				if (flag_count == len(eql_grps)):
					oi = oi + 1
	
	########################
	#	Checking for allenes
	########################
	for i in c_atoms:
		if ((i.tot_no == 2) and (i.is_ct == 0)):
			flag = 0
			for j in i.neighbours:
				if (j.tot_no == 3):
					temp_parent = j.number - 1
					roots = []
					for k in str_class_arr[j.number-1].neighbours:
						if (k.number == (i.number-1)):
							continue
						roots.append(k)
					for k in roots:
						k.create_children(temp_parent)
					flag = flag + roots[0].compare_subgraph(roots[1])
			if (flag == 2):
				oi = oi + 1
						
				
	
	
	####################
	#	Checking -O-O- psuedochiral centres
	####################
	temp = []
	for i in range(na):
		if (atoms[i+1] == 'O'):
			for j in range(na):
				if (bonds[i][j] == 1):
					if (atoms[j+1] == 'O'):
						if (((i,j) not in temp) and ((j,i) not in temp)):
							temp.append((i,j))
							oi = oi + 1
							
	return (oi)
				
						
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
