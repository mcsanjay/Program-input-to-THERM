


class carbon():
	def __init__(self):
		self.symbol = 'C'
		self.number = 0
		self.tot_no = 0					#Total no of neighbouring atoms
		self.c_no = 0
		self.o_no = 0
		self.h_no = 0
		self.is_cd = 0
		self.is_ct = 0
		self.neighbours = []
		
	def print_all(self):
		print (self.number,self.c_no,self.h_no,self.is_cd)
		
	def print_neighbours(self):
		self.print_all()
		print("Neighbours :")
		for i in self.neighbours:
			i.print_all()


class hydrogen():
	def __init__(self):
		self.symbol = 'H'
		self.number = 0
		self.neighbours = []


class oxygen():
	def __init__(self):
		self.symbol = 'O'
		self.number = 0
		self.is_cd = 0
		self.neighbours = []

class atom_string():
	def __init__(self):
		self.number = 0
		self.symbol = ''
		self.string = ""
		self.neighbours = []
		self.parent = 0
		self.child = []
	
	def create_children (self,prnt_no):
		self.child = []
		for i in self.neighbours:
			if (i.number == prnt_no):
				self.parent = i
			else:
				self.child.append(i)
		
		for i in self.child:
			i.create_children(self.number)
	
	def check_similarity (self,r2):
		root1 = list(self.child)
		root2 = list(r2.child)	
		eql_grps = []
		r1_children = []
		r2_children = []
		for i in root1:
			r1_children.append(i.string)
		for i in root2:
			r2_children.append(i.string)
		if (len(r1_children) != len(r2_children)):
			return ([[]])
		else:
			a_and_b = set(r1_children) & set(r2_children)
			a = r1_children
			b = r2_children
			if ((set(a) | set(b)) != (set(a) & set(b))):
				return ([[]])
			if ((len(set(a)) == len(a_and_b)) and (len(set(b)) == len(a_and_b))):
				for i in a_and_b:
					if (a.count(i) != b.count(i)):
						return ([[]])
				####################
				if (len(a) == (len(set(a)) + 2)):
					for i in range(3):
						#temp = []
						if (i == 0):
							q1 = 1
							q2 = 2
						elif (i == 1):
							q1 = 2
							q2 = 0
						elif (i == 2):
							q1 = 0
							q2 = 1
						temp = [(root1[0],root2[i]),(root1[1],root2[q1]),(root1[2],root2[q2])]
						eql_grps.append(list(temp))
						temp = [(root1[0],root2[i]),(root1[1],root2[q2]),(root1[2],root2[q1])]
						eql_grps.append(list(temp))
				#################
					'''if (len(a) == len(set(a))):
						temp = []
						for i in a:
							x = a.index(i)
							y = b.index(i)
							temp.append((root1[x],root2[y]))
						eql_grps.append(temp)     '''
				#####################
				else:
					temp = []

					temp_a = list(a)
					temp_b = list(b)
					gr = []
					for i in temp_a:
						for j in temp_b:
							if (i == j):
								temp.append((temp_a.index(i),temp_b.index(j)))
								temp_b[temp_b.index(j)] = '0'
								temp_a[temp_a.index(i)] = '1'
								break

					gr.append(list(temp))

					temp = []

					temp_a = list(a)
					temp_b = list(b)
					for i in temp_a:
						
						for j in range(len(temp_b)):
							
							if (i == temp_b[j]):
								if ((temp_a.index(i),j) in gr[0]):
									continue
								temp.append((temp_a.index(i),j))
								temp_b[j] = '0'
								temp_a[temp_a.index(i)] = '1'
								break

					for i in a:
						if (a.count(i) == 1):
							temp.append((a.index(i),b.index(i)))
					for i in range(len(temp)-1):
						for j in range(i+1,len(temp)):
							if(temp[i][0]>temp[j][0]):
								t = temp[i]
								temp[i] = temp[j]
								temp[j] = t 

					gr.append(list(temp))

					if (gr[0] == gr[1]):
						gr.remove(gr[1])
						
					temp = []
					for i in gr:
						for j in i:
							temp.append((root1[j[0]],root2[j[1]]))
						eql_grps.append(list(temp))
		
			return (eql_grps)
			
			
	def compare_subgraph (self,r2):				# flag = 1 for different
		if (self.string != r2.string):
			return (1)
		elif ((self.string ==  r2.string) and (self.child == [])):
			return (0)
		else:
			flag = 0
			eql_grps = self.check_similarity(r2)
			if (eql_grps == [[]]):
				flag = 1
				return (flag)
			else:
				for i in eql_grps:
					for j in i:
						#print(eql_grps)
						flag = j[0].compare_subgraph(j[1])
						if (flag == 1):
							break
					if (flag == 0):
						break
				return (flag)
				
		
		
				
								




