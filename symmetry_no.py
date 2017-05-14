
import copy
#import all_classes
import optical_isomer

def calc_symm_no_current (temp, parent_no, s_no):
	temp_str = []
	for k in temp:
		temp_str.append(k.string)
	
	eql_grps = optical_isomer.similar_groups(temp_str)
	if ((len(eql_grps) == 3) or ((len(eql_grps) == 1) and (len(temp_str) == 2))):
		flag_count = 0
		for k in eql_grps:
			temp1 = []
			for l in k:
				temp1.append(temp[l])
			for l in temp1:
				l.create_children(parent_no)
				
			flag = temp1[0].compare_subgraph(temp1[1])
			flag_count = flag_count + flag
		if (flag_count == 0):
			#print(s_no,len(temp))
			s_no = s_no * len(temp)
				
	return (s_no)
	

#def check_subgraph_sim (str_class_arr,root,parent)
#	str_class_arr[root].create_children(parent)
#	flag = str_class_arr[i].compare_subgraph(str_class_arr[j])

def calc_symm_no (atoms, bonds, c_atoms, str_class_arr, na, rad, rad_atom):
	parent_s_no = 1
	temp_bonds = []
	for i in range(na):
		if (atoms[i+1] != 'C'):
			continue
		for j in range(na):
			if (bonds[i][j] == 1):
				if (((i,j) in temp_bonds) or ((j,i) in temp_bonds)):
					continue
				temp_bonds.append((i,j))
				if (atoms[j+1] == 'H'):
					continue
				
				else:
					temp_c = [str_class_arr[i],str_class_arr[j]]
					for k in temp_c:
						if (k.symbol == 'O'):
							continue
						if (len(k.neighbours) < 3):
							continue
						temp = []
						for l in temp_c:
							if (k.number == l.number):
								continue
							temp_no = l.number
						for l in k.neighbours:
							if (l.number == temp_no):
								continue
							temp.append(l)
						parent_s_no = calc_symm_no_current(temp,k.number,parent_s_no)
						
	if (rad == 1):
		if (parent_s_no % 2 != 0):
			if (len(str_class_arr[rad_atom-1].neighbours) == 3):
				flag_rad = 0
				roots = []
				for i in str_class_arr[rad_atom-1].neighbours:
					if ((flag_rad == 0) and (i.symbol == 'H')):
						flag_rad = 1
						continue
					roots.append(i)
				roots[0].create_children(rad_atom-1)
				roots[1].create_children(rad_atom-1)
				flag_rad = roots[0].compare_subgraph(roots[1])
				if (flag_rad == 0):
					parent_s_no = parent_s_no * 2
					
		if (parent_s_no % 2 != 0):
			parent_root = []
			root1 = str_class_arr[rad_atom-1]
			for i in str_class_arr[rad_atom-1].neighbours:
				if ((len(i.neighbours) == 3) and (i.symbol == 'C')):
					parent_root.append(i)
			
			for i in parent_root:
				flag5 = 0
				for j in range(na):
					if ((bonds[i.number][j] == 2) and (atoms[j+1] == str_class_arr[rad_atom-1].symbol)):
						root2 = str_class_arr[j]
						flag5 = 1
						break
				if (flag5 == 1):
					temp_root2_string = root2.string
					root2.string = "RADICAL"
					root1.create_children(i.number)
					root2.create_children(i.number)
					flag3 = root1.compare_subgraph(root2)
					root2.string = temp_root2_string
					if (flag3 == 0):
						parent_s_no = parent_s_no * 2
						break
						
		
	
	if (rad == 0):
		temp = []
		flag0 = 0
		for i in range(na):
			if (atoms[i+1] == 'H'):
				continue
			for j in range(na):
				if (bonds[i][j] > 0):
					if (atoms[j+1] == 'H'):
						continue
					else:
						if (((i,j) in temp) or ((j,i) in temp)):
							continue
						else:
							temp.append((i,j))
							str_class_arr[i].create_children(j)
							str_class_arr[j].create_children(i)
							flag = str_class_arr[i].compare_subgraph(str_class_arr[j])
							if (flag == 0):
								flag0 = 1
								
								# Branched trans
								if (bonds[i][j] == 2):
									flag_trans = 0
									temp_par = str_class_arr[i]
									while True:
										temp_child = []
										
										for k in temp_par.child:
											if (k.symbol != 'H'):
												temp_child.append(k)
										
										if (len(temp_child) == 0):
											break
										elif (len(temp_child) == 1):
											temp_par = temp_child[0]
										elif (len(temp_child) == 2):
											flag_trans = 1
											break
										elif (len(temp_child) == 3):
											combi = [[[0,1],2],[[0,2],1],[[1,2],0]]
											for k in combi:
												flag_temp = temp_child[k[0][0]].compare_subgraph(temp_child[k[0][1]])
												if (flag_temp == 0):
													temp_par = temp_child[k[1]]
													break
											if (flag_temp == 1):
												flag_trans = 1
												break
									if (flag_trans == 0):
										parent_s_no = parent_s_no * 2
								else:
									parent_s_no = parent_s_no * 2
									break
			if (flag0 == 1):
				break
		
		if (flag0 == 0):
			all_combi = [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
			for i in range(na):
				#if (str_class_arr[i].string == "RADICAL"):
				#	if (len(str_class_arr[i].neighbours) < 3):
				#		continue
				#	else:
						
						
				
				if (atoms[i+1] == 'H'):
					continue
				elif (atoms[i+1] == 'C'):
					flag1 = 0
					for k in c_atoms:
						if (k.number == (i+1)): 
							if ((k.tot_no == 2) and (k.is_ct == 0)):
								flag1 = 2
							elif (k.tot_no == 3):
								flag1 = 3
							elif (k.tot_no == 4):
								flag1 = 4
					if (flag1 == 2):
						roots = []
						for j in range(na):
							if (bonds[i][j] == 2):
								roots.append(str_class_arr[j])
						roots[0].create_children(i)
						roots[1].create_children(i)
						flag3 = roots[0].compare_subgraph(roots[1])
						if (flag3 == 0):
							parent_s_no = parent_s_no * 2
							break
					
					elif (flag1 == 3):
						roots = []
						#flag2 = 0
						for j in range(na):
							if (bonds[i][j] == 1):
							#	if (atoms[j+1] == 'H'):
							#		flag2 = 1
							#		break
							#	else:
								roots.append(str_class_arr[j])
							elif (bonds[i][j] == 2):
								temp_double_atom = str_class_arr[j]
						#if (flag2 == 1):
						#	continue
						#print(c_atoms)
						roots[0].create_children(i)
						roots[1].create_children(i)
						flag3 = roots[0].compare_subgraph(roots[1])
						if (flag3 == 0):
							if (temp_double_atom.symbol == 'O'):
								print(parent_s_no)
								parent_s_no = parent_s_no * 2
								break
							else:
								flag4 = 0
								parent_no = i
								while True:
									temp_double_atom.create_children(parent_no)
									parent_no = temp_double_atom.number
									
									if (len(temp_double_atom.child) == 2):
										#temp_children = temp_double_atom.child
										for j in temp_double_atom.child:
											j.create_children(parent_no)
										flag4 = temp_double_atom.child[0].compare_subgraph(temp_double_atom.child[1])
										break
									elif (len(temp_double_atom.child) == 1):
										if (temp_double_atom.child[0].symbol == 'O'):
											break
										else:
											temp_double_atom = temp_double_atom.child[0]
								if (flag4 == 0):
									print(parent_s_no)
									parent_s_no = parent_s_no * 2 
									break
										
					elif (flag1 == 4):
						neigh_grps = []
						for j in range(na):
							if (bonds[i][j] == 1):
								neigh_grps.append(str_class_arr[j])
						#print(i+1)
						for j in all_combi:
							flag2 = 0
							for k in j:
								
								neigh_grps[k[0]].create_children(i)
								neigh_grps[k[1]].create_children(i)
								flag3 = neigh_grps[k[0]].compare_subgraph(neigh_grps[k[1]])
								flag2 = flag2 + flag3
							if (flag2 == 0):
								parent_s_no = parent_s_no * 2
								break
				elif (atoms[i+1] == 'O'):
					roots = []
					flag2 = 0
					for j in range(na):
						if (bonds[i][j] == 2):
							flag2 = 1
							break
						if (bonds[i][j] == 1):
							roots.append(str_class_arr[j])
					if (flag2 == 1):
						continue
					roots[0].create_children(i)
					roots[1].create_children(i)
					flag3 = roots[0].compare_subgraph(roots[1])
					if (flag3 == 0):
						parent_s_no = parent_s_no * 2
						break
	return (parent_s_no)

def symm_no (atoms, bonds, c_atoms, na, rad, rad_atom):
	
	atom_str = optical_isomer.string_atoms(bonds,atoms,na)
	
	str_class_arr = optical_isomer.create_string_class(bonds,atoms,atom_str,na)
	
	parent_s_no = calc_symm_no(atoms,bonds,c_atoms,str_class_arr,na,0,0)
	
	#print(parent_s_no)
	if (rad == 1):
		t_na = na - 1
		for i in c_atoms:
			if (i.number == rad_atom):
				i.h_no = i.h_no - 1
				i.tot_no = i.tot_no - 1
				break
		
		for i in str_class_arr:
			if (i.number == (rad_atom-1)):
				i.string = "RADICAL"
				for j in i.neighbours:
					if (j.symbol == 'H'):
						temp_rad_h = j.number
						i.neighbours.remove(j)
						break
				break
		
		t_bonds = copy.deepcopy(bonds)
		del t_bonds[temp_rad_h]
		for i in t_bonds:
			del i[temp_rad_h]
		t_atoms = atoms.copy()
		del t_atoms[temp_rad_h+1]
		if ((temp_rad_h+1) != na):
			for i in range((temp_rad_h+1),na):
				t_atoms[i] = t_atoms[i+1]
			del t_atoms[na]

		rad_s_no = calc_symm_no(t_atoms,t_bonds,c_atoms,str_class_arr,t_na,rad,rad_atom)
		
		for i in c_atoms:
			if (i.number == rad_atom):
				i.h_no = i.h_no + 1
				i.tot_no = i.tot_no + 1
				break
	
		return (parent_s_no,rad_s_no)
		
	
	return (parent_s_no)
					
