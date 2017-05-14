
def bond_dissoc (atoms, bonds, c_atoms, na, rad_atom):
	
	bd = []
	if (atoms[rad_atom] == 'C'):
		bd_order = ["C#CJ","C#CCJC2","C#CCJC","C#CCJ","C*C*CJC","C*C*CJ","C*CJC*C","C*CCJC*C","C*CJOR","CJOOH","CJOC*O","VINS","VIN","CJCHO","C2CJOR","C2CJOH","CJOR","CJOH","ALLYLT","ALLYLS","ALLYLP","T","S","P"]
		for i in c_atoms:
			if (i.number == rad_atom):
				rad_c = i
				break
		
		if ((rad_c.h_no-1) >= 2):
			bd.append("P")
		
		if ((rad_c.h_no-1) == 1):
			if (rad_c.is_cd == 0):
				bd.append("S")
		
		if ((rad_c.h_no-1) == 0):
			if ((rad_c.tot_no-1) == 3):
				bd.append("T")
		
		if ((rad_c.h_no-1) == 1):
			#print (rad_c.h_no)
			if (((rad_c.tot_no-1) == 2) and (rad_c.o_no == 0)):
				bd.append("VIN")
		
		if ((rad_c.h_no-1) == 0):
			if ((rad_c.tot_no-1) == 2):
				for i in range(na):
					if (bonds[rad_atom-1][i] == 2):
						if (atoms[i+1] == 'C'):
							bd.append("VINS")
							break
		
		if ((rad_c.h_no-1) == 2):
			if (rad_c.o_no == 0):
				temp = rad_c.neighbours[0].number
				if (rad_c.neighbours[0].tot_no == 3):
					for i in range(na):
						if (bonds[temp-1][i] == 2):
							if (atoms[i+1] == 'C'):
								bd.append("ALLYLP")
								break
		
		if ((rad_c.h_no-1) == 1):
			if ((rad_c.tot_no-1) == 3):
				for i in rad_c.neighbours:
					if (i.tot_no == 3):
						flag = 0
						for j in range(na):
							if (bonds[i.number-1][j] == 2):
								if (atoms[j+1] == 'C'):
									bd.append("ALLYLS")
									flag = 1
									break
						if (flag == 1):
							break
		
		if ((rad_c.h_no-1) == 0):
			if ((rad_c.tot_no-1) == 3):
				flag = 0
				for i in rad_c.neighbours:
					if (i.tot_no == 3):	
						for j in range(na):
							if (bonds[i.number-1][j] == 2):
								if (atoms[j+1] == 'C'):
									bd.append("ALLYLT")
									flag = 1
									break
						if (flag == 1):
							break
		
		if (rad_c.is_ct == 1):
			bd.append("C#CJ")
		
		if (rad_c.c_no == 1):
			if (rad_c.neighbours[0].is_ct == 1):
				bd.append("C#CCJ")
		
		if (rad_c.c_no == 2):
			for i in rad_c.neighbours:
				if (i.is_ct == 1):
					bd.append("C#CCJC")
					break
		
		if (rad_c.c_no == 3):
			for i in rad_c.neighbours:
				if (i.is_ct == 1):
					bd.append("C#CCJC2")
					break
		
		if ((rad_c.tot_no-1) == 2):
			if (rad_c.c_no == 1):
				if ((rad_c.neighbours[0].tot_no == 2) and (rad_c.neighbours[0].is_ct == 0)):
					if (rad_c.neighbours[0].o_no == 0):
						bd.append("C*C*CJ")
		
		if ((rad_c.tot_no-1) == 2):
			if (rad_c.c_no == 2):
				for i in rad_c.neighbours:
					if ((i.tot_no == 2) and (i.is_ct == 0)):
						if (i.o_no == 0):
							bd.append("C*C*CJC")
							break
		
		if (((rad_c.h_no-1) == 0) and (rad_c.o_no == 0)):
			if ((rad_c.tot_no-1) == 2):
				flag = 0
				#print (bonds)
				for i in range(na):
					if (bonds[rad_atom-1][i] == 1):
						if (atoms[i+1] == 'C'):
							for j in c_atoms:
								if (j.number == (i+1)):
									if (j.tot_no == 3):
										for k in range(na):
											if (bonds[j.number-1][k] == 2):
												if (atoms[k+1] == 'C'):
													bd.append("C*CJC*C")
													flag = 1
													break
								if (flag == 1):
									break
					if (flag == 1):
						break
		
		if (rad_c.c_no == 2):
			if ((rad_c.tot_no-1) == 3):
				flag = 0
				for i in rad_c.neighbours:
					if (i.tot_no == 3):
						for j in range(na):
							if (bonds[i.number-1][j] == 2):
								if (atoms[j+1] == 'C'):
									flag = flag + 1
									break
				if (flag == 2):
					bd.append("C*CCJC*C")
		
		if ((rad_c.c_no == 0) or (rad_c.c_no == 1)):	
			if (rad_c.o_no > 0):
				flag1 = 0
				flag2 = 0
				for i in range(na):
					if (bonds[rad_atom-1][i] == 1):
						if (atoms[i+1] == 'O'):
							for j in range(na):
								if ((bonds[i][j] == 1) and (rad_atom != (j+1))):
									if (atoms[j+1] == 'H'):
										if (flag1 == 0):
											bd.append("CJOH")
											flag1 = 1
									elif (atoms[j+1] == 'C'):
										if (flag2 == 0):
											bd.append("CJOR")
											flag2 = 1
								if ((flag1 == 1) and (flag2 == 1)):
									break
					if ((flag1 == 1) and (flag2 == 1)):
						break
		
		if (rad_c.o_no > 0):
			flag = 0
			for i in range(na):
				if (bonds[rad_atom-1][i] == 1):
					if (atoms[i+1] == 'O'):
						for j in range(na):
							if ((bonds[i][j] == 1) and (rad_atom != (j+1))):
								if (atoms[j+1] == 'C'):
									for k in range(na):
										if (bonds[j][k] == 2):
											if (atoms[k+1] == 'O'):
												bd.append("CJOC*O")
												flag = 1
												break
							if (flag == 1):
								break
				if (flag == 1):
					break
		
		if ((rad_c.c_no == 2) and (rad_c.o_no == 1)):
			flag1 = 0
			flag2 = 0
			for i in range(na):
				if (bonds[rad_atom-1][i] == 1):
					if (atoms[i+1] == 'O'):
						for j in range(na):
							if ((bonds[i][j] == 1) and (rad_atom != (j+1))):
								if (atoms[j+1] == 'H'):
									bd.append("C2CJOH")
									flag1 = 1
									break
								elif (atoms[j+1] == 'C'):
									bd.append("C2CJOR")
									flag2 = 1
									break
				if ((flag1 == 1) and (flag2 == 1)):
					break
		
		for i in rad_c.neighbours:
			if (bonds[rad_c.number-1][i.number-1] != 1):
				continue
			if (i.c_no == 1):
				if (i.o_no == 1):
					if (i.h_no == 1):
						bd.append("CJCHO")
						break
		
		if (rad_c.o_no > 0):
			flag = 0
			for i in range(na):
				if (bonds[rad_atom-1][i] == 1):
					if (atoms[i+1] == 'O'):
						for j in range(na):
							if ((bonds[i][j] == 1) and (rad_atom != (j+1))):
								if (atoms[j+1] == 'O'):
									for k in range(na):
										if ((bonds[j][k] == 1) and (i != k)):
											if (atoms[k+1] == 'H'):
												bd.append("CJOOH")
												flag = 1
												break
							if (flag == 1):
								break
				if (flag == 1):
					break
		
		if ((rad_c.tot_no-1) == 2):
			if (rad_c.o_no == 1):
				flag = 0
				for j in range(na):
					if (bonds[rad_atom-1][j] == 1):
						if (atoms[j+1] == 'O'):
							for k in range(na):
								if ((bonds[j][k] == 1) and (rad_atom != (k+1))):
									if (atoms[k+1] == 'C'):
										bd.append("C*CJOR")
										flag = 1
										break
					if (flag == 1):
						break
		
		
		for i in bd_order:
			if (i in bd):
				return (i)
				
	##############################
	if (atoms[rad_atom] == 'O'):
		bd_order = ["ALPEROX","OJC*OC","VINOXY","ALKOXY"]
		for i in range(na):
			if (bonds[rad_atom-1][i] == 1):
				if (atoms[i+1] == 'H'):
					continue
				n = i
				break
				
		if (atoms[n+1] == 'C'):
			bd.append("ALKOXY")
			
		if (atoms[n+1] == 'C'):
			for j in range(na):
				if (bonds[n][j] == 2):
					if (atoms[j+1] == 'C'):
						bd.append("VINOXY")
						break
		
		if (atoms[n+1] == 'C'):
			for j in c_atoms:
				if (j.number == (n+1)):
					temp = j
					break
			if (temp.h_no == 0):
				if (temp.tot_no == 3):
					if ((temp.c_no == 1) and (temp.o_no == 2)):
						for i in range(na):
							if (bonds[temp.number-1][i] == 2):
								if (atoms[i+1] == 'O'):
									bd.append("OJC*OC")
								break
		
		if (atoms[n+1] == 'O'):
			for i in range(na):
				if ((bonds[n][i] == 1) and (rad_atom != (i+1))):
					if (atoms[i+1] == 'C'):
						bd.append("ALPEROX")
					break
		
		for i in bd_order:
			if (i in bd):
				return (i)		

		
							
							
		
		
		
								
		
									
			
					
	
	
	
