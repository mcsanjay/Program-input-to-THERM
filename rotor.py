
import resonance

def no_of_rotors (atoms, bonds, c_atoms, na, rad, rad_atom):
	parent_rot = 0
	rad_rot = 0

	for i in range(na):
		for j in range(i,na):
			if (bonds[i][j] == 1):
				if ((atoms[i+1] == 'H') or (atoms[j+1] == 'H')):
					continue
				else:
					parent_rot = parent_rot + 1
	if (rad == 0):
		return (parent_rot)
	elif (rad == 1):
		rad_rot = parent_rot
		res_eff = resonance.resonance_eff(atoms,bonds,c_atoms,na,rad_atom)
		rad_rot = rad_rot - res_eff
		if (atoms[rad_atom] == 'O'):
			if (res_eff == 0):
				rad_rot = parent_rot - 1
		
		return ((parent_rot,rad_rot))
		
