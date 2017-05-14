#!/usr/bin/env python
import sys

flag = 0
'''
if ("-o" not in sys.argv):
	if ("-s" in sys.argv):
		if ((len(sys.argv) == 3) or (len(sys.argv) == 4) or (len(sys.argv) == 6)):
			flag = 0
		else:
			flag = 1
	elif ("-sf" in sys.argv):
		if ((len(sys.argv) == 3) or (len(sys.argv) == 5)):
			flag = 0
		else:
			flag = 1
	elif ("-mf" in sys.argv):
		if ((len(sys.argv) == 3) or (len(sys.argv) == 4) or (len(sys.argv) == 6)):
			flag = 0
		else:
			flag = 1
	else:
		flag = 1
else:
	i = sys.argv.index("-o")
	if (len(sys.argv) <= (i+1)):
		flag = 1
	elif (sys.argv[i+1][0] == '-'):
		flag = 1
	elif ("-s" in sys.argv):
		if ((len(sys.argv) == 5) or (len(sys.argv) == 6)):
			flag = 0
		else:
			flag = 1
	elif ("-sf" in sys.argv):
		if (len(sys.argv) == 5):
			flag = 0
		else:
			flag = 1
	elif ("-mf" in sys.argv):
		if ((len(sys.argv) == 5) or (len(sys.argv) == 6)):
			flag = 0
		else:
			flag = 1
	else:
		flag = 1

if ("-doc" in sys.argv):
	i = sys.argv.index("-doc")
	if (len(sys.argv) <= (i+1)):
		flag = 1
	elif (sys.argv[i+1][0] == '-'):
		flag = 1
'''

if (("-s" in sys.argv) or ("-sf" in sys.argv) or ("-mf" in sys.argv)):
	flag = 0
else:
	flag = 1

if ("-s" in sys.argv):
	if (len(sys.argv) == (sys.argv.index("-s") + 1)):
		flag = 1
	elif (sys.argv[sys.argv.index("-s") + 1][0] == '-'):
		flag = 1
		
if ("-sf" in sys.argv):
	if (len(sys.argv) == (sys.argv.index("-sf") + 1)):
		flag = 1
	elif (sys.argv[sys.argv.index("-sf") + 1][0] == '-'):
		flag = 1
		
if ("-mf" in sys.argv):
	if (len(sys.argv) == (sys.argv.index("-mf") + 1)):
		flag = 1
	elif (sys.argv[sys.argv.index("-mf") + 1][0] == '-'):
		flag = 1		
		
if ("-o" in sys.argv):
	if (len(sys.argv) == (sys.argv.index("-o") + 1)):
		flag = 1
	elif (sys.argv[sys.argv.index("-o") + 1][0] == '-'):
		flag = 1

if ("-doc" in sys.argv):
	if (len(sys.argv) == (sys.argv.index("-doc") + 1)):
		flag = 1
	elif (sys.argv[sys.argv.index("-doc") + 1][0] == '-'):
		flag = 1

if (flag == 1):
	print (
	'''\n{}
	   -s	<"SMILES string"> <"Name">
	   -sf	<SMILES_file>
	   -mf	<molfile> <"Name">
	   -o	<output_filename (.LST file) (without extension)>
	   -doc	<output_filename (.DOC file) (without extension)>\n'''.format(sys.argv[0]))
	sys.exit()




print ("\nImporting modules ...")

import os
from rdkit import Chem

import main


def check_ring (m):
	ri = m.GetRingInfo()
	return ri.NumRings()


out_file_path = None	

if ("-o" in sys.argv):
	i = sys.argv.index("-o")
	out_file_name = sys.argv[i+1]
	therm_config = open("./therm.config",'r')
	lines = therm_config.readlines()
	therm_config.close()
	for i in lines:
		words = i.split()
		if (len(words) == 0):
			continue
		if (words[0][0] == '#'):
			continue
		if (words[0] == "OUTPUT_FOLDER"):
			if ((len(words) < 3) or (words[2][0] == '#')):
				print('\nError : Output folder not specified in "therm.config" !!!\n')
				sys.exit()
			if (not (os.path.isdir(words[2]))):
				print("\cError : Could not find output folder !!!\n")
				sys.exit()
			out_fol = words[2]
			break
	if (out_fol[-1] != '/'):
		out_fol = out_fol + '/'
	out_file_path = out_fol + out_file_name[0:8] + ".LST"
	out_file = open(out_file_path,'w')
	out_file.write(" UNITS:KCAL\n")
	out_file.write(" {}\n".format(out_file_name))
	out_file.write(" SPECIES       Hf       S    Cp 300     400     500     600     800     1000     1500     DATE        ELEMENTS")
	out_file.close()


doc_file_path = None
if ("-doc" in sys.argv):
	i = sys.argv.index("-doc")
	doc_file_name = sys.argv[i+1]
	therm_config = open("./therm.config",'r')
	lines = therm_config.readlines()
	therm_config.close()
	for i in lines:
		words = i.split()
		if (len(words) == 0):
			continue
		if (words[0][0] == '#'):
			continue
		if (words[0] == "OUTPUT_FOLDER"):
			if ((len(words) < 3) or (words[2][0] == '#')):
				print('\nError : Output folder not specified in "therm.config" !!!\n')
				sys.exit()
			if (not (os.path.isdir(words[2]))):
				print("\cError : Could not find output folder !!!\n")
				sys.exit()
			out_fol = words[2]
			break
	if (out_fol[-1] != '/'):
		out_fol = out_fol + '/'
	doc_file_path = out_fol + doc_file_name + ".DOC"
	doc_file = open(doc_file_path,'w')
	doc_file.write("{}\n".format(doc_file_name))
	doc_file.close()
	
	
if ("-s" in sys.argv):
	i = sys.argv.index("-s")
	
	m = Chem.MolFromSmiles(sys.argv[i+1])
	if (len(sys.argv) > (i+2)):
		if (sys.argv[3][0] != '-'):
			name = sys.argv[3][:9]
		else:
			name = "Molecule"
	else:
		name = "Molecule"
		
	print ("\n==========================================")
	print ("\nName : {}".format(name))
		
	if (m == None):
		print ("\nWrong SMILES...\nCannot process species...")
		print ("\n==========================================\n")
		sys.exit(1)
	n_rings = check_ring (m)
	if (n_rings > 0):
		print ("\nThis is a cyclic species !!!\nProgram exiting...")
		print ("\n==========================================\n")
		sys.exit(1)
	m_blk = Chem.MolToMolBlock(m)
	#print (m_blk)
	lines = m_blk.split('\n')
	if (len(sys.argv) > (i+2)):
		if (sys.argv[3][0] != '-'):
			name = sys.argv[3][:9]
		else:
			name = "Molecule"
	else:
		name = "Molecule"
	#print(lines)
	main.main_prog(lines,name,out_file_path,doc_file_path)
	print ("\n==========================================\n")

elif (sys.argv[1] == "-sf"):			#SMILES		NAME
	s_file = open(sys.argv[sys.argv.index("-sf") + 1],'r')
	m_lines = s_file.readlines()
	s_file.close()
	i = 0	
	for l in m_lines:
		m_splt = l.split()
		if (len(m_splt) == 0):
			continue
		elif (m_splt[0][0] == '#'):
			continue
		i = i + 1
		m = Chem.MolFromSmiles(m_splt[0])
		bd_grp = None
		if (len(m_splt) > 1):
			if (m_splt[1][0] != '#'):
				if (m_splt[1] == '*'):
					name = "Mol" + str(i)
				else:
					name = m_splt[1][:9]
				
			if (len(m_splt) > 2):
				if (m_splt[2][0] != '#'):
					bd_grp = m_splt[2]
		else:
			name = "Mol" + str(i)
		
		print ("\n==========================================")
		print ("\nName : {}".format(name))
		
		if (m == None):
			print ("\nWrong SMILES...\nSkipping species...")
			print ("\n==========================================\n")
			continue
		n_rings = check_ring (m)
		if (n_rings > 0):
			print ("\nThis is a cyclic species !!!\nSkipping species...")
			print ("\n==========================================\n")
			continue
		m_blk = Chem.MolToMolBlock(m)
		lines = m_blk.split('\n')
		
		main.main_prog(lines,name,out_file_path,doc_file_path,bd_grp)
		print ("\n==========================================\n")


elif (sys.argv[1] == "-mf"):
	i = sys.argv.index("-mf")
	
	mol_file = open(sys.argv[sys.argv.index("-mf") + 1],'r')
	lines = mol_file.readlines()
	mol_file.close()
	if (len(sys.argv) > (i+2)):
		if (sys.argv[3][0] != '-'):
			name = sys.argv[3][:9]
		else:
			name = "Molecule"
	else:
		name = "Molecule"
	main.main_prog(lines,name,out_file_path,doc_file_path)
	print ("\n==========================================\n")
	
print ("Program exited !!!\n")
		
