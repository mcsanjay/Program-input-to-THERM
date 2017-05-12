


def no_of_gauche(c_atoms, c_c_bonds):
	flag = 0
	for i in c_c_bonds:
		if (i[1] > 1):
			(g_ane, g_ene) = alkene_yne_gauche(c_atoms,c_c_bonds)
			flag = 1
			break
		'''elif (i[1] == 3):
			(g_ane, g_ene) = alkyne_gauche(c_atoms,c_c_bonds)
			flag = 2
			break'''
	if (flag == 0):
		for i in c_atoms:
			if ((i.is_cd == 1) or (i.is_ct == 1)):
				(g_ane, g_ene) = alkene_yne_gauche(c_atoms,c_c_bonds)
				flag = 2
				break
	if (flag == 0):			
		(g_ane, g_ene) = alkane_gauche(c_atoms,c_c_bonds)
	return (g_ane, g_ene)
	
	
def alkane_gauche(c_atoms, c_c_bonds):
	gauche = 0
	for i in c_c_bonds:
		if (i[1] == 1):
			temp_c_no = []
			for j in c_atoms:
				if (j.number in i[0]):
					temp_c_no.append(j.c_no)
			if (temp_c_no == [3,2] or temp_c_no == [2,3]):
				gauche = gauche + 1
			elif (temp_c_no == [4,2] or temp_c_no == [2,4]):
				gauche = gauche + 2
			elif (temp_c_no == [3,3]):
				gauche = gauche + 2
			elif (temp_c_no == [3,4] or temp_c_no == [4,3]):
				gauche = gauche + 4
			elif (temp_c_no == [4,4]):
				gauche = gauche + 6
			#print(temp_c_no,gauche) 
	
	return (gauche, 0)


def alkene_gauche(c_atoms, c_c_bonds):
	g_ane = 0
	g_ene = 0
	cd_c = []
	for i in c_atoms:
		if (i.is_cd == 1):
			cd_c.append(i.number)
	#print (cd_c)
	for i in c_c_bonds:
		if (i[1] == 1):
			temp_c_no = []
			for j in c_atoms:
				if (j.number in i[0]):
					temp_c_no.append(j.c_no)
					
			#print(temp_c_no,g_ane)
			
			if ((i[0][0] not in cd_c) and (i[0][1] not in cd_c)):
				if (temp_c_no == [3,2] or temp_c_no == [2,3]):
					g_ane = g_ane + 1
				elif (temp_c_no == [4,2] or temp_c_no == [2,4]):
					g_ane = g_ane + 2
				elif (temp_c_no == [3,3]):
					g_ane = g_ane + 2
				elif (temp_c_no == [3,4] or temp_c_no == [4,3]):
					g_ane = g_ane + 4
				elif (temp_c_no == [4,4]):
					g_ane = g_ane + 6
				#print(temp_c_no,g_ane)
			
			elif (((i[0][0] in cd_c) and (i[0][1] not in cd_c)) or ((i[0][0] not in cd_c) and (i[0][1] in cd_c))):
				flag = 0
				for c in c_atoms:
					if ((c.number == i[0][0]) or (c.number == i[0][1])):
						cd_c_no = c.c_no
						if (c.h_no == 0):
							if (c.o_no == 0):
								flag = 1
							elif (c.o_no == 1):
								for bond in c_c_bonds:
									if ((c.number in bond[0]) and (bond[1] == 2)):
										flag = 2
					if (flag != 0):
						break
				
				if ((flag == 1) or (flag == 2)):
					if (2 in temp_c_no):
						g_ene = g_ene + 1
					elif (temp_c_no == [3,3]):
						g_ene = g_ene + 2
					elif (4 in temp_c_no):
						g_ene = g_ene + 2
				#print(temp_c_no,g_ane)
	
	return (g_ane,g_ene)




#### Alkyne ####

def alkene_yne_gauche(c_atoms, c_c_bonds):
	g_ane = 0
	g_ene = 0
	cd_c = []
	ct_c = []
	for i in c_atoms:
		if (i.is_cd == 1):
			cd_c.append(i.number)
		elif (i.is_ct == 1):
			ct_c.append(i.number)
	#print (cd_c)
	for i in c_c_bonds:
		if (i[1] == 1):
			temp_c_no = []
			for j in c_atoms:
				if (j.number in i[0]):
					temp_c_no.append(j.c_no)
					
			#print(temp_c_no,g_ane)
			
			if ((i[0][0] not in (cd_c + ct_c)) and (i[0][1] not in (cd_c + ct_c))):
				if (temp_c_no == [3,2] or temp_c_no == [2,3]):
					g_ane = g_ane + 1
				elif (temp_c_no == [4,2] or temp_c_no == [2,4]):
					g_ane = g_ane + 2
				elif (temp_c_no == [3,3]):
					g_ane = g_ane + 2
				elif (temp_c_no == [3,4] or temp_c_no == [4,3]):
					g_ane = g_ane + 4
				elif (temp_c_no == [4,4]):
					g_ane = g_ane + 6
				#print(temp_c_no,g_ane)
			
			elif (((i[0][0] in cd_c) and (i[0][1] not in (cd_c + ct_c))) or ((i[0][0] not in (cd_c + ct_c)) and (i[0][1] in cd_c))):
				flag = 0
				for c in c_atoms:
					if (((c.number == i[0][0]) or (c.number == i[0][1])) and (c.is_cd == 1)): 
						cd_c_no = c.c_no
						if (c.h_no == 0):
							if (c.o_no == 0):
								flag = 1
							elif (c.o_no == 1):
								for bond in c_c_bonds:
									if ((c.number in bond[0]) and (bond[1] == 2)):
										flag = 2
					if (flag != 0):
						break
				
				if ((flag == 1) or (flag == 2)):
					if (2 in temp_c_no):
						g_ene = g_ene + 1
					elif (temp_c_no == [3,3]):
						g_ene = g_ene + 2
					elif (4 in temp_c_no):
						g_ene = g_ene + 2
				#print(temp_c_no,g_ane)
	
	return (g_ane,g_ene)


