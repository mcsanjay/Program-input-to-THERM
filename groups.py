
def group_string (grp):
	grp_str = ""
	for i in grp:
		if (i[1] == 0):
			continue
		else:
			grp_str = grp_str + '/' + i[0] + str(i[1])
	grp_str = grp_str.replace('1','')
	return (grp_str)

def current_group (i, skip_atoms, atoms, bonds, na):
	curr_grp = [["C",0],["CD",0],["CO",0],["CT",0],["H",0],["O",0],["OO",0]]
	curr_grp[4][1] = i.h_no									#H
	#print(atoms)
	#print(bonds)
	for j in i.neighbours:
		if (j.number in skip_atoms):
			continue
		if (j.tot_no == 4):									#C
			curr_grp[0][1] = curr_grp[0][1] + 1
		if (j.tot_no == 3):
			for k in range(na):
				if (bonds[j.number-1][k] == 2):
					#print(atoms[j.number])
					if (atoms[k+1] == 'O'):					#CO
						curr_grp[2][1] = curr_grp[2][1] + 1
					else:									#CD
						curr_grp[1][1] = curr_grp[1][1] + 1
					break
		if (j.tot_no == 2):									#CT
			curr_grp[3][1] = curr_grp[3][1] + 1
	for k in range(na):
		if (bonds[i.number-1][k] > 0):
			if ((atoms[k+1] == 'O') and ((k+1) not in skip_atoms)):
				oo = 0
				for l in range(na):
					if (bonds[k][l] > 0):
						if (atoms[l+1] == 'O'):
							oo = 1
							break
				if (oo == 0):								#O
					curr_grp[5][1] = curr_grp[5][1] + 1
				else:										#OO
					curr_grp[6][1] = curr_grp[6][1] + 1 
	
	grp_str = group_string (curr_grp)
	return (grp_str)

def current_group_o (o_no, skip_atoms, atoms, bonds, na):
	curr_grp = [["C",0],["CD",0],["CO",0],["CT",0],["H",0]]
	for p in o_no:
		for i in range(na):
			if ((i+1) in skip_atoms):
				continue
			if ((bonds[p-1][i] == 1) and ((i+1) not in o_no)):
				if (atoms[i+1] == 'H'):
					curr_grp[4][1] = curr_grp[4][1] + 1					#H
				elif (atoms[i+1] == 'C'):
					count = 0
					for j in range(na):
						if (bonds[i][j] == 3):
							curr_grp[3][1] = curr_grp[3][1] + 1			#CT
							break
						elif (bonds[i][j] == 2):
							if (atoms[j+1] == 'C'):
								curr_grp[1][1] = curr_grp[1][1] + 1		#CD
							else:
								curr_grp[2][1] = curr_grp[2][1] + 1		#CO
							break
						elif (bonds[i][j] == 1):
							count = count + 1
					if (count == 4):
						curr_grp[0][1] = curr_grp[0][1] + 1				#C

	grp_str = group_string (curr_grp)
	return (grp_str)
						
	
def list_groups (atoms, bonds, c_atoms, na):
	grps = []
	#	FOR CARBON GROUPS
	flag = 0
	for i in c_atoms:
		skip_atoms = []
		
		if (i.tot_no == 4):
			flag = 1
			temp_grp_str = current_group(i,skip_atoms,atoms,bonds,na)
			
		elif (i.tot_no == 3):
			for j in range(na):
				if (bonds[i.number-1][j] == 2):
					skip_atoms.append(j+1)
					if (atoms[j+1] == 'C'):
						flag = 2
					else:
						flag = 3
					break
			temp_grp_str = current_group(i,skip_atoms,atoms,bonds,na)
			
		elif (i.tot_no == 2):
			if (i.is_ct == 1):
				flag = 4
				for j in range(na):
					if (bonds[i.number-1][j] == 3):
						skip_atoms.append(j+1)
						break
				temp_grp_str = current_group(i,skip_atoms,atoms,bonds,na)
			elif (i.o_no == 0):
				flag = 5
			elif (i.o_no == 1):
				flag = 6
		
		if (flag == 1):
			grp_str = "C" + temp_grp_str
		elif (flag == 2):
			grp_str = "CD" + temp_grp_str
		elif (flag == 3):
			grp_str = "CO" + temp_grp_str
		elif (flag == 4):
			grp_str = "CT" + temp_grp_str
		elif (flag == 5):
			grp_str = "CA"
		elif (flag == 6):
			grp_str = "KETENE"
		
		# MAKING /CO2/ TO /CO/CO/
		grp_splt = grp_str.split('/')
		if (grp_splt[0] == 'C'):
			if ("CO2" in grp_splt):
				grp_str = "C"
				for i in range(1,len(grp_splt)):
					if (grp_splt[i] == "CO2"):
						grp_str = grp_str + "/CO/CO"
					else:
						grp_str = grp_str + '/' + grp_splt[i]
		
		grps.append(grp_str)
	
	#	FOR OXYGEN GROUPS
	temp_o = []
	for i in range(na):
		flag1 = 0
		no_o = 0
		if (atoms[i+1] == 'O'):
			if ((i+1) in temp_o):
				continue
			for j in range(na):
				if (bonds[i][j] == 2):
					flag1 = 1
					break
				if (bonds[i][j] == 1):
					if (atoms[j+1] == 'O'):
						no_o = no_o + 1
			if (flag1 == 1):
				continue
			
			else:
				temp_o.append(i+1)
				if (no_o == 0):
					temp_grp_str = current_group_o([(i+1)],[],atoms,bonds,na)
					grp_str = "O" + temp_grp_str
					
				elif (no_o == 1):
					triple_o = 0
					for j in range(na):
						if ((bonds[i][j] == 1) and (atoms[j+1] == 'O')):
							sec_o = j
							for k in range(na):
								if ((bonds[j][k] == 1) and (i != k)):
									if (atoms[k+1] == 'O'):
										#sec_o = j						#SECOND OXYGEN
										triple_o = 1
										break
									else:
										temp_o.append(j+1)
										#sec_o = j						#SECOND OXYGEN
										break
							break
								
					if (triple_o == 0):
						temp_grp_str = current_group_o([(i+1),(sec_o+1)],[],atoms,bonds,na)
						grp_str = "OO" + temp_grp_str
					elif (triple_o == 1):
						temp_grp_str = current_group_o([(i+1)],[(sec_o+1)],atoms,bonds,na)
						grp_str = "O" + temp_grp_str + "/O"
						
				elif (no_o == 2):
					grp_str = "O/O2"
						
				grps.append(grp_str)
	
	#	SORTING AND FINDING NO OF EACH GROUPS	
	temp = []		
	grps_sort = []
	for i in grps:
		if (i not in temp):
			grps_sort.append([i,grps.count(i)])
			temp.append(i)
									
	return (grps_sort)
	
			
					
