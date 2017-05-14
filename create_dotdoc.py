
def create_doc (g_ane, g_ene, h_repel_no, oi, grps, rotors, symm_no, bd, no_of_c, no_of_o, no_of_h, name, rad, doc_file_path):
	doc_file = open(doc_file_path,'a')
	print ("\nWriting .DOC file...")
	doc_file.write("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
	doc_file.write("NAME = {}".format(name))
	doc_file.write("\nFORMULA = ")
	if (no_of_c != 0):
		doc_file.write("C{}".format(no_of_c))
	if (no_of_o != 0):
		doc_file.write("O{}".format(no_of_o))
	if (no_of_h != 0):
		doc_file.write("H{}".format(no_of_h))
	
	tot_grps = 0
	for i in grps:
		tot_grps = tot_grps + i[1]
	tot_grps = tot_grps + g_ane + g_ene + h_repel_no + oi
	if (rad == 1):
		tot_grps = tot_grps + 1
	doc_file.write("\nTOTAL NO. OF GROUPS = {}".format(tot_grps))
	
	doc_file.write("\n\nGROUPS :")
	for i in grps:
		doc_file.write("\n{}\t{}".format(i[0],i[1]))
	if (g_ane != 0):
		doc_file.write("\nGAUCHE\t{}".format(g_ane))
	if (g_ene != 0):
		doc_file.write("\nGAUCHE/E\t{}".format(g_ene))
	if (h_repel_no != 0):
		doc_file.write("\cH/REPEL/15\t{}".format(h_repel_no))
	if (oi != 0):
		doc_file.write("\nOI\t{}".format(oi))
	if (rad == 1):
		doc_file.write("\n{}".format(bd))
	
	if (rad == 1):
		doc_file.write("\n\nPARENT ROTOR NO. = {}\nRADICAL ROTOR NO. = {}".format(rotors[0],rotors[1]))
		doc_file.write("\n\nPARENT SYMMETRY NO. = {}\nRADICAL SYMMETRY NO. = {}".format(symm_no[0],symm_no[1]))
	else:
		doc_file.write("\n\nROTOR NO. = {}".format(rotors))
		doc_file.write("\n\nSYMMETRY NO. = {}".format(symm_no))
	
	doc_file.write("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
	
	doc_file.close()
	print ("Successfully written .DOC file !!!")
	
