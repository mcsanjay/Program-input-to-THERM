import sys
import os
import math
import time

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def update_values (values,lines,look4,no):
	flag = 0
	for i in lines:
		w = i.split()
		if (len(w) < 9):
			continue
		if (w[0][-1] == ','):
			temp = w[0][:-1]
		else:
			temp = w[0]
		
		if (temp in look4):
			flag = 1
			for k in range(8):
				values[k] = values[k] + float(w[k+1])*no
			if (len(w) == 9):
				values[8] = None
			if (values[8] != None):
				if (is_number(w[9])):
					values[8] = values[8] + float(w[9])*no
				else:
					values[8] = None
			break
	return (flag)

def create_lstfile (values, no_c, no_o, no_h, rotors, name, rad, out_file_path):
	if (values[8] == None):
		val_8 = ".00"
	else:
		val_8 = values[8]
	curr_date = time.strftime("%m/%d/%y")
	if (rad == 0):
		rot = rotors
	else:
		rot = rotors[1]
	
	
	fout = open(out_file_path,'a')
	fout.write("\n {0:<9} {1:>7}  {2:>7}  {3:>7} {4:>7} {5:>7} {6:>7} {7:>7} {8:>7} {9:>7}  {10:>8} THERM   C {11:>3} H {12:>3} O {13:>3} N   0 G{14:>2}".format(name,values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],val_8,curr_date,no_c,no_h,no_o,rot))
	fout.close()

def create_dotlst (g_ane, g_ene, h_15, oi, grps, rotors, symm_no, bd, no_c, no_o, no_h, name, rad, out_file_path):
	f = open("therm.config",'r')
	lines = f.readlines()
	f.close()
	for i in lines:
		words = i.split()
		if (len(words) == 0):
			continue
		if (words[0][0] == '#'):
			continue
		else:
			if (words[0] == "PATH_TO_THERM"):
				pathtotherm = words[2]
				if (pathtotherm[-1] != '/'):
					pathtotherm = pathtotherm + '/'
			elif (words[0] == "HC_GROUPS_FILENAME"):
				hc = words[2]
			elif (words[0] == "HCO_GROUPS_FILENAME"):
				hco = words[2]
			elif (words[0] == "INT_GROUPS_FILENAME"):
				intf = words[2]
			elif (words[0] == "BD_GROUPS_FILENAME"):
				bdf = words[2]
			elif (words[0] == "R"):
				if (is_number(words[2])):
					R = float(words[2])
				else:
					print('\nError : Could not read R value from "therm.config" !!!\n')
					return
			elif (words[0] == "hf_H"):
				if (is_number(words[2])):
					hf_H = float(words[2])
				else:
					print('\nError : Could not read hf_H value from "therm.config" !!!\n')
					return
			elif (words[0] != "OUTPUT_FOLDER"):
				print ('\nError : In "therm.config", "{}" was a complete surprise for me !!!\n'.format(i[:-1]))
				sys.exit(0)
	
	if (not (os.path.isdir(pathtotherm))):
		print ('\nError : Cannot find THERM folder !!!\n')
		return
	
	path_hc = pathtotherm + hc
	path_hco = pathtotherm + hco
	path_int = pathtotherm + intf
	path_bd = pathtotherm + bdf
	
	if (not (os.path.isfile(path_hc))):
		print ("\nError : Cannot find HC file !!!\n")
		return
	if (not (os.path.isfile(path_hco))):
		print ("\nError : Cannot find HCO file !!!\n")
		return
	if (not (os.path.isfile(path_int))):
		print ("\nError : Cannot find INT file !!!\n")
		return
	if (not (os.path.isfile(path_bd))):
		print ("\nError : Cannot find BD file !!!\n")
		return
		
	fhc = open(path_hc,'r')
	fhco = open(path_hco,'r')
	fint = open(path_int,'r')
	fbd = open(path_bd,'r')
	
	hc_lines = fhc.readlines()
	hco_lines = fhco.readlines()
	int_lines = fint.readlines()
	bd_lines = fbd.readlines()
	
	fhc.close()
	fhco.close()
	fint.close()
	fbd.close()
	
	values = [0,0,0,0,0,0,0,0,0]
	#R = 1.987	# cal/molK
	
	for i in grps:
		look4 = [i[0]]
		flag = 0
		if ('O' in i[0]):
			flag = update_values(values,hco_lines,look4,i[1])
		else:
			flag = update_values(values,hc_lines,look4,i[1])
		if (flag == 0):
			print('\nError : Could not find "{}" group in THERM !!!'.format(i[0]))
			return
	
	look4 = ["GAUCHE","GAUCHE/A"]
	flag_ga = update_values(values,int_lines,look4,g_ane)
	if (flag_ga == 0):
		print ('\nError : Could not find "GAUCHE" group in THERM !!!')
		return
		
	look4 = ["GAUCHE/E"] 
	flag_ge = update_values(values,int_lines,look4,g_ene)
	if (flag_ge == 0):
		print ('\nError : Could not find "GAUCHE/E" group in THERM !!!')
		return
		
	look4 = ["OI"]
	flag_oi = update_values(values,int_lines,look4,oi)
	if (flag_oi == 0):
		print ('\nError : Could not find "OI" group in THERM !!!')
		return
		
	look4 = ["H/REPEL/15","H15"]
	flag_h15 = update_values(values,int_lines,look4,h_15)
	if (flag_h15 == 0):
		print ('\nError : Could not find "H/REPEL/15" group in THERM !!!')
		return
	
	for i in range(8):
		values[i] = round(values[i],2)
	if (values[8] != None):
		values[8] = round(values[8],2)
	
	look4 = [bd]
	if (rad == 1):
		#hf_H = 52.103	# kcal/mol
		hf_parent = values[0]
		flag_bd = update_values(values,bd_lines,look4,1)
		if (flag_bd == 0):
			print('\nError : Could not find "{}" group in THERM !!!'.format(bd))
			return
		delh_rxn = round(values[0],2) - hf_parent
		values[0] = values[0] - hf_H
		values[0] = round(values[0],2)
	
	for i in range(8):
		values[i] = round(values[i],2)
	if (values[8] != None):
		values[8] = round(values[8],2)
	
	if (rad == 0):
		values[1] = values[1] - R*math.log(symm_no)
		values[1] = round(values[1],2)
	else:
		values[1] = values[1] - R*math.log(symm_no[1])
		values[1] = round(values[1],2)
	
	#print (values)
	
	print ("\nWriting to file...")
	create_lstfile(values,no_c,no_o,no_h,rotors,name,rad,out_file_path)
	print ("Successfully written to file !!!")			
	
	
	
	
	
