
import sys
from select import select
#from rdkit import Chem

import data_process
import groups
import rotor
import symmetry_no
import gauche
import h_repel
import optical_isomer
import bond_dissociation
import all_classes
import create_dotlst
#################################

def main_prog (lines, name = None, out_file_path = None):
	
	(lines,na,nb,rad,rad_atom) = data_process.d_process(lines)

	#print (na,nb)

	atoms = {}
	i = 4

	for j in range(na):
		words = lines[i].split()
		for k in words:
			if (k.isalpha()):
				atoms[i-3] = k
				break
		i = i+1
	#print (atoms)

	#n = (len(atoms))

	bonds = []
	c_c_bonds = []
	for i in range(na):
		bonds.append([])
		for j in range(na):
			bonds[i].append(0)

	i = 4 + na
	k = 0
	for j in range(nb):
		flag2 = 0
		words = lines[i].split()
		
		if ((lines[i][0] == ' ') and (len(words[0]) > 2)):
			a = int(words[0][0:2]) - 1
			b = int(words[0][2:]) - 1
			flag2 = 1
		elif ((lines[i][0] != ' ') and (len(words[0]) > 3)):
			a = int(words[0][0:3]) - 1
			b = int(words[0][3:]) - 1
			flag2 = 1
		else:
			a = int(words[0]) - 1
			b = int(words[1]) - 1
		
		if (flag2 == 0):
			#print (words)
			bonds[a][b] = int(words[2])
			bonds[b][a] = int(words[2])
			if (atoms[a+1] == 'C' and atoms[b+1] == 'C'):
				c_c_bonds.append([])
				c_c_bonds[k] = [(a+1,b+1),int(words[2])]
				k = k + 1
		elif (flag2 == 1):
			#print (words)
			bonds[a][b] = int(words[1])
			bonds[b][a] = int(words[1])
			if (atoms[a+1] == 'C' and atoms[b+1] == 'C'):
				c_c_bonds.append([])
				c_c_bonds[k] = [(a+1,b+1),int(words[1])]
				k = k + 1
		i = i+1

		

	c_atoms = []
	h_atoms = []
	o_atoms = []

	def create_carbon ():
		q = all_classes.carbon()
		c_atoms.append(q)

	def create_hydrogen ():
		q = all_classes.hydrogen()
		h_atoms.append(q)

	def create_oxygen ():
		q = all_classes.oxygen()
		o_atoms.append(q)


	no_of_c = 0
	no_of_h = 0
	no_of_o = 0

	for i in range(na):
		if (atoms[i+1]=='H'):
			create_hydrogen()
			h_atoms[no_of_h].number = i+1
			no_of_h = no_of_h + 1
		elif (atoms[i+1]=='O'):
			create_oxygen()
			o_atoms[no_of_o].number = i+1
			no_of_o = no_of_o + 1
		elif (atoms[i+1]=='C'):
			create_carbon()
			c_atoms[no_of_c].number = i+1
			no_of_c = no_of_c + 1
			
	for i in c_atoms:
		for j in range(na):
			if (bonds[i.number-1][j] != 0):
				i.tot_no = i.tot_no + 1
				if (atoms[j+1] == 'C'):
					i.c_no = i.c_no + 1
					for k in c_atoms:
						if (k.number == j+1):
							i.neighbours.append(k)
					if (bonds[i.number-1][j] == 2):
						i.is_cd = 1
					elif (bonds[i.number-1][j] == 3):
						i.is_ct = 1
				if (atoms[j+1] == 'H'):
					i.h_no = i.h_no + 1
				if (atoms[j+1] == 'O'):
					i.o_no = i.o_no + 1
					if (bonds[i.number-1][j] > 1):
						i.is_cd = 1

	

	#print ("\n==========================================")
	
	#print ("\nName : {}".format(name))
	##################################
	#	GAUCHE
	##################################
			
	(gauche_ane, gauche_ene) = gauche.no_of_gauche(c_atoms,c_c_bonds)
	
	#print ("\nalkane gauche = {}, and alkene gauche = {}".format(gauche_ane,gauche_ene))

	print ("\ngauche = {}".format(gauche_ane))

	##################################
	#	H_REPEL_15
	##################################

	h_repel_no = h_repel.h_repel(c_atoms)

	#print ("\nH_repel_15 = {}".format(h_repel_no))

	##################################
	#	OPTICAL ISOMERISM
	##################################

	oi = optical_isomer.opt_isomer(c_atoms,bonds,atoms,na)

	print ("\nOptical Isomers = {}".format(oi))

	##################################
	#	GROUPS
	##################################

	grps = groups.list_groups(atoms,bonds,c_atoms,na)

	print ("\nGroups : \n{}".format(grps))

	##################################
	#	ROTORS
	##################################

	rotors = rotor.no_of_rotors(atoms,bonds,c_atoms,na,rad,rad_atom)

	print ("\nNo. of rotors = {}".format(rotors))

	##################################
	#	SYMMETRY NUMBER
	##################################
	
	symm_no = symmetry_no.symm_no(atoms,bonds,c_atoms,na,rad,rad_atom)
	
	print ("\nSymmetry no = {}".format(symm_no))
	
	##################################
	#	BD
	##################################
	
	if (rad == 1):
		bd = bond_dissociation.bond_dissoc(atoms,bonds,c_atoms,na,rad_atom)
		
		print ("\nbd = {}".format(bd))
		
		
		if (out_file_path != None):
			timeout = 5
			print ("\nDo you want to enter some other BD group?? (if yes, press Enter)")
			inp,_,_ = select([sys.stdin], [], [], timeout)
			if (inp):
				lin = sys.stdin.readline()
				#if ((lin[0] == 'y') or (lin[0] == 'Y')):
				bd = raw_input("\nEnter BD group (case sensitive): ")
				#else:
				#	print("\nContinuing with the same BD group...")
			else:
				print("\nContinuing with the same BD group...")
			
				
	else:
		bd = None
		
	
	
	##################################
	#print ("\n==========================================\n")
	
	##########================########
	#	CREATE .LST
	##########================########
	
	if (out_file_path != None):
		create_dotlst.create_dotlst(gauche_ane,gauche_ene,h_repel_no,oi,grps,rotors,symm_no,bd,no_of_c,no_of_o,no_of_h,name,rad,out_file_path)
	
	
	

