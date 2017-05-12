import optical_isomer

def resonance_eff (atoms, bonds, c_atoms, na, rad_atom):
	res_eff = 0
	atom_str = optical_isomer.string_atoms(bonds,atoms,na)
	str_class_arr = optical_isomer.create_string_class(bonds,atoms,atom_str,na)
	root1 = rad_atom
	for i in range(na):
		if (bonds[rad_atom-1][i] == 1):
			if (atoms[i+1] == 'C'):
				flag_is_cd = 0
				for l in c_atoms:
					if (l.number == (i+1)) :
						if (l.is_cd == 1):
							flag_is_cd = 1
				if (flag_is_cd == 1):
					parent_c = i+1
					for j in range(na):
						if ((bonds[i][j] == 2) and (atoms[j+1] == atoms[rad_atom])):
							root2 = j+1
							atom_str = optical_isomer.string_atoms(bonds,atoms,na)
							atom_str[root1-1] = "RADICAL"
							atom_str[root2-1] = "RADICAL"
							str_class_arr = optical_isomer.create_string_class(bonds,atoms,atom_str,na)
							for k in str_class_arr[root1-1].neighbours:
								if (k.symbol == 'H'):
									str_class_arr[root1-1].neighbours.remove(k)
									break
							r1 = str_class_arr[root1-1]
							r2 = str_class_arr[root2-1]
							r1.create_children(parent_c-1)
							r2.create_children(parent_c-1)
							flag = r1.compare_subgraph(r2)
							if (flag == 0):
								res_eff = res_eff + 1
								
	return (res_eff)
