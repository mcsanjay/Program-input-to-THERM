
def d_process (lines):	
	
	w = lines[3].split()
	if ((lines[3][0] == ' ') and (len(w[0]) > 2)):
		na = int(w[0][0:2])
		nb = int(w[0][2:])
	elif ((lines[3][0] != ' ') and (len(w[0]) > 3)):
		na = int(w[0][0:3])
		nb = int(w[0][3:])
	else:
		na = int(w[0])
		nb = int(w[1])
	
	hedr = lines[0:4]
	a_blk = lines[4:(na+4)]
	bnd_blk = lines[(na+4):(na+nb+4)]
	
	######################################
	#	CHECK FOR RADICAL
	######################################
	rad = 0
	rad_atom = 0
	for i in lines:
		words = i.split()
		if (len(words) < 5):
			continue
		if ((words[0] == 'M') and (words[1] == "RAD")):
			rad = 1
			if ((int(words[2]) > 1) or (int(words[4]) > 2)):
				print ("\nNOT A SINGLE RADICAL !!!\n")
				exit(1)
			rad_atom = int(words[3])
			break
	#####################################
	#	MOLFILE WITH HYDROGEN AND NO 'M RAD' LINE BUT STILL A RADICAL
	#####################################	
	if (rad == 0):
		h_no = 0
		for i in lines:
			words = i.split()
			if (len(words) < 4):
				continue
			if (words[3] == 'H'):
				h_no = h_no + 1
		if ((h_no%2) == 1):
			rad = 1
			for i in range(na):
				if (a_blk[i].split()[3] == 'C'):
					val = 4
				elif (a_blk[i].split()[3] == 'O'):
					val = 2
				else:
					print("\n\n{} WAS A COMPLETE SURPRISE FOR ME !!!\n\n".format(a_blk[i].split()[3]))
					exit()
				count = 0
				for j in range(nb):
					temp_words = bnd_blk[j].split()
					if (((i+1) == int(temp_words[0])) or ((i+1) == int(temp_words[1]))):
						count = count + int(temp_words[2])
				if (count < val):
					rad_atom = i+1
					break
					
	############################################
	#	FOR MOLFILES NOT HAVING HYDROGEN ATOMS
	############################################
	flag = 0
	for i in a_blk:
		if (i.split()[3] == 'H'):
			flag = 1
			break
	if (flag == 0):
		tot_na = na
		tot_nb = nb
		for i in range(na):
			if (a_blk[i].split()[3] == 'C'):
				val = 4
			elif (a_blk[i].split()[3] == 'O'):
				val = 2
			else:
				print("\n\n{} WAS A COMPLETE SURPRISE FOR ME !!!\n\n".format(a_blk[i].split()[3]))
				exit()
			count = 0
			for j in range(nb):
				temp_words = bnd_blk[j].split()
				if (((i+1) == int(temp_words[0])) or ((i+1) == int(temp_words[1]))):
					count = count + int(temp_words[2])
			if (count < val):
				for k in range((val-count)):
					tot_na = tot_na + 1
					a_blk.append("0.0000 0.0000 0.0000 H")
					tot_nb = tot_nb + 1
					bnd_blk.append("{} {} 1".format((i+1),tot_na))
		na = tot_na
		nb = tot_nb
		temp = "{} {}".format(na,nb)
		del hedr[-1]
		hedr.append(temp)
		lines = []
		lines = hedr + a_blk + bnd_blk				
	
	##############################################
	#	FOR RADICAL MOLFILES WITH HYDROGEN
	##############################################
	elif ((flag == 1) and (rad == 1)):
		na = na + 1
		nb = nb + 1
		a_blk.append("0.0000 0.0000 0.0000 H")
		bnd_bld.append("{} {} 1".format(rad_atom,na))
		temp = "{} {}".format(na,nb)
		del hedr[-1]
		hedr.append(temp)
		lines = []
		lines = hedr + a_blk + bnd_blk	
	#############################################
	#print(lines)
	return (lines,na,nb,rad,rad_atom)
