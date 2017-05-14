
Install RDKit, 
Open terminal and type : 
	sudo apt-get install python-rdkit

Initial setup of the program...

1. Put all files into one folder.

2. Open 'therm.config' and edit it appropriately.

Running the porgram...

1. Open terminal and change directory to the folder containing the program.

2. Make the file 'Auto_THERM.py' executable. Type :
	chmod +x Auto_THERM.py

3. Running the program for a single species using SMILES. Type :
	./Auto_THERM.py -s "<SMILES_of_the_species>"

   Running the program for a single species using molfile. Type :
	./Auto_THERM.py -mf <Path_to_Molfile>

   Running the program for many species, i.e., a text file containing many SMILES. Type :
	./Auto_THERM.py -sf <Path_to_SMILES_text_file>

4. Obtaining output file (.LST). Type :
	-o <Output_LST_filename_without_extension>
   along with other arguments to 'Auto_THERM.py'

5. Obtaining output file (.DOC). Type :
	-doc <Output_DOC_filename_without_extension>
   along with other arguments to 'Auto_THERM.py'

