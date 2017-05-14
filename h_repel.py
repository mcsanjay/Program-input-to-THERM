
'''
def h_repel(c_atoms, c_c_bonds):
	c_chain = []
	c1 = []
	c2 = []
	c3 = []
	h_repel_no = 0
	flag = 0 
	#c_4c = []
	for i in c_atoms:
		if (i.c_no == 4):
			c_chain.append(i.number)
			#c1.append(i)
			for j in i.neighbours:
				if ((j.c_no > 1) and (j.tot_no == 4)):
					c_chain.append(j.number)
					for k in j.neighbours:
						if ((k.c_no < 3) or (k.number in c_chain) or (k.tot_no < 4)):
							continue
						elif (k.c_no == 3):
							c_chain.append(k.number)
							for l in k.neighbours:
								if ((l.number in c_chain) or (l.tot_no < 4)):
									flag = flag + 1
									continue
								else:
									if (l.h_no > 0):
										h_repel_no = h_repel_no + 1
						


def h_repel(c_atoms):

	h_repel_no = 0
	
	for i in c_atoms:
		if (i.c_no == 4):
			c1 = []					# [R,L,F,B]	
			c2 = []
			c3 = []
			for j in i.neighbours:
				c1.append(j)
			for j in range(4):
				if ((c1[j].c_no > 1) and (c1[j].tot_no == 4)):
					for k in c1[j].neighbours:
							c2.append(k)
					if ((j % 2) == 0):
						if (c2[j+1].number != i.number):
							for k in range(4):
								if (c2[k].number == i.number):
									temp = c2[k]
									c2[k] = c2[j+1]
									c2[j+1] = temp
									break
					else:
						if (c2[j-1].number != i.number):
							for k in range(4):
								if (c2[k].number == i.number):
									temp = c2[k]
									c2[k] = c2[j-1]
									c2[j-1] = temp
									break
						
						
def h_repel(c_atoms):
	h_repel_no = 0
	for i in c_atoms:
		if (i.c_no == 4):
			c1=[]
			h_count = []
			for j in i.neighbours:
				c1.append(j)
				h_count.append(j.h_no)
			flag = 0
			for j in h_count:
				if (j > 0):
					flag = 1
					break
			if (flag == 0):
				continue
			for j in c1:
				if ((j.is_cd == 1) or (j.is_ct == 1)):
					continue
				elif (j.c_no == 2):
					for k in j.neighbours:
						if ((k.is_cd == 1) or (k.is_ct == 1)):
							break
						elif (k.number == i.number):
							continue
						else:
							if (k.c_no == 3):
								flag = 0
								for l in k.neighbours:
									if (l.number == j.number):
										continue
									elif ((l.is_cd == 1) or (l.is_ct == 1)):
										flag = 0
										break
									elif (l.h_no > 1):
											flag = flag + 1
								if (flag > 0):
									h_repel_no = h_repel_no + 1
							elif (k.c_no == 4):
								if (k.number > i.number):
									cdt_no = 0
									flag = 0
									for l in k.neighbours:
										if (l.number == j.number):
											continue
										elif ((l.is_cd == 1) or (l.is_ct == 1)):
											cdt_no = cdt_no + 1
										elif (l.h_no > 1):
											flag = flag + 1
									if (cdt_no == 0):
										if (flag == 1):
											h_repel_no = h_repel_no + 1
										elif ((flag == 2) or (flag == 3)):
											h_repel_no = h_repel_no + 2
									elif (cdt_no == 1):
										if ((flag == 1) or (flag == 2)):
											h_repel_no = h_repel_no + 1
						
########################

def explore_c3 (



def h_repel(c_atoms):
	h_repel_no = 0
	for i in c_atoms:
		if (i.c_no == 4):
			pos = -1
			c1=[]
			h_count = []
			for j in i.neighbours:
				c1.append(j)				# [R,L,F,B]
				h_count.append(j.h_no)
			
			flag = 0
			for j in h_count:
				if (j > 0):
					flag = 1
					break
			if (flag == 0):
				continue
				
			for j in range(3):
				k = j + 1
				while (k < 4):
					if (c1[j].c_no < c1[k].c_no):
						temp = c1[j]
						c1[j] = c1[k]
						c1[k] = temp
						temp = h_count[j]
						h_count[j] = h_count[k]
						h_count[k] = temp
					k = k + 1
			
			
			pos = -1
			for j in c1:
				pos = pos + 1
				if ((j.is_cd == 1) or (j.is_ct == 1)):
					continue
				elif (j.c_no == 2):
					if ((pos == 0) or (pos == 1)):
						a = 2
						b = 3
					else:
						a = 0
						b = 1
					for k in j.neighbours:
						if ((k.is_cd == 1) or (k.is_ct == 1)):
							break
						elif (k.number == i.number):
							continue
						else:
							
							if (k.c_no == 3):
								#c3 = []					# R,B
								flag = 0
								for l in k.neighbours:
									if (l.number == j.number):
										continue
									elif ((l.is_cd == 1) or (l.is_ct == 1)):
										flag = 0
										break
									elif ((l.h_no > 1) and (l.o_no > 0)):
										flag = 0
										break
									elif ((l.h_no > 1) and (l.o_no == 0)):
										flag = flag + 1
								if (flag > 0):
									if ((c1[a].tot_no == 4) and (c1[b].tot_no == 4)):
										if ((c1[a].h_no > 1) and (c1[b].h_no > 1)):
											if ((c1[a].o_no == 0) and (c1[b].o_no == 0)):
												h_repel_no = h_repel_no + 1
										
							elif (k.c_no == 4):
								if (k.number > i.number):
									cdt_no = 0
									flag = 0
									flag_ch3 = 0
									for l in k.neighbours:
										if (l.number == j.number):
											continue
										elif ((l.is_cd == 1) or (l.is_ct == 1)):
											cdt_no = cdt_no + 1
										elif ((l.h_no > 1) and (l.o_no == 0)):
											flag = flag + 1
										if (l.h_no == 3):
											flag_ch3 = flag_ch3 + 1
									if (cdt_no == 0):
										if (flag == 1):
											if ((c1[a].tot_no == 4) and (c1[b].tot_no == 4)):
												if ((c1[a].h_no > 1) and (c1[b].h_no > 1)):
													if ((c1[a].o_no == 0) and (c1[b].o_no == 0)):
														h_repel_no = h_repel_no + 1
										elif ((flag == 2) or (flag == 3)):
											for q in [2,3]:
												if (c1[q].tot_no == 4):
													if (c1[q].h_no > 1):
														if (c1[q].o_no == 0):
															h_repel_no = h_repel_no + 1
									elif (cdt_no == 1):
										if ((flag == 1) or (flag == 2)):
											if ((c1[a].tot_no == 4) and (c1[b].tot_no == 4)):
												if ((c1[a].h_no > 1) and (c1[b].h_no > 1)):
													if ((c1[a].o_no == 0) and (c1[b].o_no == 0)):
														h_repel_no = h_repel_no + 1
									
									
				elif (j.c_no == 3):  			
					c2 = []					# [R,F]
					for k in j.neighbours:
						if (k.number == i.number):
							continue
						c2.append(k)
					if (c2[0].c_no < c2[1].c_no):
						temp = c2[0]
						c2[0] = c2[1]
						c2[1] = temp
					if ((c2[0].tot_no < 4) and (c2[1].tot_no == 4)):
						temp = c2[0]
						c2[0] = c2[1]
						c2[1] = temp
					
					pos1 = -1
					for k in c2:
						pos1 = pos1 + 1
						if ((k.tot_no < 4) or (k.c_no < 3)):
							continue
						if (pos1 == 0):
							a = 3
							b = 2
						else:
							a = 1
							b = 2
						if ((k.c_no == 3) and (k.tot_no == 4)):
							for l in k.neighbours:
								
							
							
#=====================================================================#



def h_repel (c_atoms):
	h_repel_no = 0
	for i in c_atoms:
		if (i.c_no == 4):
			pos = -1
			c1=[]
			h_count = []
			for j in i.neighbours:
				c1.append(j)				# [R,L,F,B]
				h_count.append(j.h_no)
			
			flag = 0
			for j in h_count:
				if (j > 1):
					flag = 1
					break
			if (flag == 0):
				continue
			
			for j in range(3):
				k = j + 1
				while (k < 4):
					if (c1[j].c_no < c1[k].c_no):
						temp = c1[j]
						c1[j] = c1[k]
						c1[k] = temp
						temp = h_count[j]
						h_count[j] = h_count[k]
						h_count[k] = temp
					k = k + 1
			
			if ((c1[2].c_no > 2) or (c1[3].c_no > 2)):
				continue
				
			pos = -1
			for j in c1:
				pos = pos + 1
				if ((j.is_cd == 1) or (j.is_ct == 1)):
					continue
				elif (j.c_no == 2):
					if ((pos == 0) or (pos == 1)):
						a = 2
						b = 3
					else:
						a = 0
						b = 1
					for k in j.neighbours:
						if ((k.is_cd == 1) or (k.is_ct == 1)):
							break
						elif (k.number == i.number):
							continue
						else:
							
							if (k.c_no == 3):
								c3 = []
								for l in k.neighbours:
									if (l.number == j.number):
										continue
									else:
										c3.append(l)
								if (c3[0].c_no > c3[1].c_no):
									temp = c3[0]
									c3[0] = c3[1]
									c3[1] =  temp
								if ((c3[0].c_no == 1) and (c3[1].c_no == 1)):
									if (												'''
						

################==========================#######################
#				FINAL											#
##################=========================######################


def rearrange (c):
	for j in range((len(c)-1)):
		k = j + 1
		while (k < len(c)):
			if (c[j].c_no < c[k].c_no):
				temp = c[j]
				c[j] = c[k]
				c[k] = temp
			k = k + 1
	'''	if (len(c) == 4):
			if (c[1].tot_no != 4):
				if (c[0].tot_no == 4):
					if ((c[2].tot_no == 4) and (c[3].tot_no == 4)):
						if (c[1].c_no == c[2].c_no):
							temp = c[1]
							c[1] = c[2]
							c[2] = temp				'''
	if (len(c) <= 3):
		if (c[0].tot_no < 4):
			if (c[1].tot_no == 4):
				if (c[1].c_no == c[0].c_no):
					temp = c[0]
					c[0] = c[1]
					c[1] = temp
		

def create_string(c):
	c_string = "C{}H{}O{}".format(c.c_no,c.h_no,c.o_no)
	return c_string


def compare_string(c_str):
	h_rep = 0
	f1 = open("H_repulsion.txt",'r')
	lines = f1.readlines()
	if (len(c_str) == 3):
		flag = 0
		for i in lines:
			if "#2" in i:
				break
			if ((flag == 1) and (i != "")):
				words = i.split()
				c1_grp = words[0].split('/')
				if (((c_str[0] == c1_grp[0]) and (c_str[1] == c1_grp[1])) or ((c_str[0] == c1_grp[1]) and (c_str[1] == c1_grp[0]))):
					if (c_str[2] == words[1]):
						h_rep = int(words[2])
						break
			if "#1" in i:
				flag = 1
	if (len(c_str) == 4):
		flag = 0
		for i in lines:
			if ((flag == 1) and (i != "")):
				words = i.split()
				c1_grp = words[0].split('/')
				c3_grp = words[1].split('/')
				if (((c_str[0] == c1_grp[0]) and (c_str[1] == c1_grp[1])) or ((c_str[0] == c1_grp[1]) and (c_str[1] == c1_grp[0]))):
					if (((c_str[2] == c3_grp[0]) and (c_str[3] == c3_grp[1])) or ((c_str[2] == c3_grp[1]) and (c_str[3] == c2_grp[0]))):
						h_rep = int(words[2])
						break
			if "#2" in i:
				flag = 1
				
	f1.close()
	return (h_rep)
			
				


def h_repel (c_atoms):
	h_rep_no = 0
	for i in c_atoms:
		if (i.c_no == 4):
			c1 = []
			cdt = 0
			for j in i.neighbours:
				c1.append(j)
				if (j.tot_no < 4):
					cdt = cdt + 1
			if (cdt > 1):
				continue
				
			rearrange(c1)				# [R,L,F,B]
			
			pos = 0
			for j in c1:
				if (j.tot_no < 4):
					pos = pos + 1
					continue
				if ((pos == 0) or (pos == 1)):
					a = 2
					b = 3
				else:
					a = 0
					b = 1
				pos = pos + 1
				
				c2 = []
				ncdt = 0
				for k in j.neighbours:
					if (k.number == i.number):
						continue
					c2.append(k)
					if (k.tot_no == 4):
						ncdt = ncdt + 1
				if (ncdt == 0):
					continue
				
				if (len(c2) > 1):
					rearrange(c2)
				
				pos1 = 0	
				for k in c2:
					if ((k.tot_no < 4) or (k.c_no < 3)):
						pos1 = pos1 + 1
						continue
					if (pos1 == 1):
						a = 1
						b = 2
					elif (pos1 == 2):
						a = 1
						b = 3
					pos1 = pos1 + 1
					
					if (k.c_no == 4):
						if (k.number < i.number):
							continue
							
					c3 = []
					for l in k.neighbours:
						if (l.number == j.number):
							continue
						c3.append(l)
					if (len(c3) < 2):
						continue
						
					rearrange(c3)
					
					#	Create string
					
					c_str = []						# [c1f,c1b,c3f,c3b]
					
					#print (c1[a].number)
					#c_str[0] = 'a'
					c_str.append(create_string(c1[a]))
					c_str.append(create_string(c1[b]))
					c_str.append(create_string(c3[1]))
					if (len(c3) == 3):
						c_str.append(create_string(c3[2]))
					
					h_rep = compare_string(c_str)
					
					h_rep_no = h_rep_no + h_rep
					
	return (h_rep_no)
			
						
						
						
						
	
	
	
	
	
	
