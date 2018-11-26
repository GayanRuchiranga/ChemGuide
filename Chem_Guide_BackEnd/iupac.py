from flask import json, jsonify
from textwrap import wrap
count = ["meth", "eth", "prop", "but", "pent", "hex",
         "hept", "oct", "non", "dec", "undec", "dodec"]


def structure_to_name(mol):
    if(int(alcohol(mol)) == 1):
        carbon = carbon_count(mol)
        return count[carbon-1]+"anol"

    elif(int(alkane(mol)) == 1):
        carbon = carbon_count(mol)
        return count[carbon-1]+"ane"

    elif(int(alkene(mol)) == 1):
        carbon = carbon_count(mol)
        return count[carbon-1]+"ene"

    elif(int(alkyne(mol)) == 1):
        carbon = carbon_count(mol)
        return count[carbon-1]+"yen"

    elif(int(ester(mol)) == 0):
        carbon = carbon_count(mol)
        return count[carbon-1]+"anoate"

    elif(int(ketone(mol)) == 0):
        carbon = carbon_count(mol)
        return count[carbon-1]+"one"

    elif(int(amine(mol)) == 1):
        carbon = carbon_count(mol)
        return count[carbon-1]+"amine"

    elif(int(amide(mol)) == 1):
        carbon = carbon_count(mol)
        return count[carbon-1]+"anoic"

    elif(int(acid_halide(mol)) == 0):
        if (mol.find("COCl") > 0):
            carbon = carbon_count(mol)
            return count[carbon-1]+"anoyl"+" "+"Chloride"

        elif (mol.find("COBr") > 0):
            carbon = carbon_count(mol)
            return count[carbon-1]+"anoyl"+" "+"Bromide"

        elif (mol.find("COI") > 0):
            carbon = carbon_count(mol)
            return count[carbon-1]+"anoyl"+" "+"Iodide"

        elif (mol.find("COF") > 0):
            carbon = carbon_count(mol)
            return count[carbon-1]+"anoyl"+" "+"Fluoride"

    elif(int(alkyl_halide(mol)) == 0):
        if (mol.find("Cl") > 0):
            carbon = carbon_count(mol)
            return count[carbon-1]+"yl"+" "+"Chloride"

        elif(mol.find("Br") > 0):
            carbon = carbon_count(mol)
            return count[carbon-1]+"yl"+" "+"Bromide"

        elif(mol.find("I") > 0):
            carbon = carbon_count(mol)
            return count[carbon-1]+"yl"+" "+"Iodide"

        elif(mol.find("F") > 0):
            carbon = carbon_count(mol)
            return count[carbon-1]+"yl"+" "+"Fluoride"
    return "Input Error"


def name_to_structure(input):
    if(alkane_name(input) != "1"):
        return alkane_name(input)
    elif(alkene_name(input) != "1"):
        return alkene_name(input)
    elif(alkyne_name(input) != "1"):
        return alkyne_name(input)
    elif(alcohol_name(input) != "1"):
        return alcohol_name(input)
    elif(ketone_name(input) != "1"):
        return ketone_name(input)
    elif(amine_name(input) != "1"):
        return amine_name(input)
    elif(amide_name(input) != "1"):
        return amide_name(input)
    elif(alkyl_halide_name(input) != "1"):
        return alkyl_halide_name(input)
    elif(acide_halide_name(input) != "1"):
        return acide_halide_name(input)


def carbon_count(input):

    input_carbon_count = 0

    for carbon in input:
        if (carbon == "c" or carbon == "C"):
            input_carbon_count += 1

    return input_carbon_count


def alcohol(input):
    carbon = 0
    hydrogen = 0
    oxygen = 0
    not_alcohol = 0
    for i in input:
        if i == "C" or i == "c":
            carbon += 1
        elif i == "H" or i == "h":
            hydrogen += 1
        elif i == "O" or i == "o":
            oxygen += 1
        elif i.isdigit():
            hydrogen += int(i)-1
        else:
            not_alcohol = 1

    if not_alcohol != 1 and hydrogen == ((carbon * 2)+2) and oxygen == 1:
        return "1"
    else:
        return "0"


def alkane(input):
    carbon = 0
    hydrogen = 0
    not_alkane = 0

    for i in input:
        if i == "C" or i == "c":
            carbon += 1
        elif i == "H" or i == "h":
            hydrogen += 1
        elif i.isdigit():
            hydrogen += int(i)-1
        else:
            not_alkane = 1

    if not_alkane != 1 and hydrogen == ((carbon * 2)+2):
        return "1"
    else:
        return "0"


def alkene(input):
    carbon = 0
    hydrogen = 0
    not_alkene = 0

    for i in input:
        if i == "C" or i == "c":
            carbon += 1
        elif i == "H" or i == "h":
            hydrogen += 1
        elif i.isdigit():
            hydrogen += int(i)-1
        else:
            not_alkene = 1

    if not_alkene != 1 and hydrogen == ((carbon * 2)):
        return "1"
    else:
        return "0"


def alkyne(input):

    carbon = 0
    hydrogen = 0
    not_alkyne = 0

    for i in input:
        if i == "C" or i == "c":
            carbon += 1
        elif i == "H" or i == "h":
            hydrogen += 1
        elif i.isdigit():
            hydrogen += int(i)-1
        else:
            not_alkyne = 1

    if not_alkyne != 1 and hydrogen == ((carbon * 2)-2):
        return "1"
    else:
        return "0"


def ester(input):

    ester_val = 0
    position = input.find("COO")

    if (input[position-3:position] == "CH3" and input[position+3:position+6] == "CH3"):
        ester_val = 0
    elif (input[position-3:position] == "CH3" and input[position+3:position+6] == "CH2"):
        ester_val = 0
    elif (input[position-3:position] == "CH3" and input[position+3:position+5] == "CH"):
        ester_val = 0
    elif (input[position-3:position] == "CH3" and input[position+3:position+5] == "CC"):
        ester_val = 0
    elif (input[position-3:position] == "CH2" and input[position+3:position+6] == "CH3"):
        ester_val = 0
    elif (input[position-3:position] == "CH2" and input[position+3:position+6] == "CH2"):
        ester_val = 0
    elif (input[position-3:position] == "CH2" and input[position+3:position+5] == "CH"):
        ester_val = 0
    elif (input[position-3:position] == "CH2" and input[position+3:position+5] == "CC"):
        ester_val = 0
    elif (input[position-2:position] == "CC" and input[position+3:position+6] == "CH3"):
        ester_val = 0
    elif (input[position-2:position] == "CC" and input[position+3:position+6] == "CH2"):
        ester_val = 0
    elif (input[position-2:position] == "CC" and input[position+3:position+5] == "CH"):
        ester_val = 0
    elif (input[position-2:position] == "CC" and input[position+3:position+5] == "CC"):
        ester_val = 0
    else:
        ester_val = 1
    return ester_val


def ketone(input):
    ketone_val = 0

    position = input.find("CO")

    if (input[position-3:position] == "CH3" and input[position+2:position+5] == "CH3"):
        ketone_val = 0
    elif (input[position-3:position] == "CH3" and input[position+2:position+5] == "CH2"):
        ketone_val = 0
    elif (input[position-3:position] == "CH3" and input[position+2:position+4] == "CH"):
        ketone_val = 0
    elif (input[position-3:position] == "CH3" and input[position+2:position+4] == "CC"):
        ketone_val = 0
    elif (input[position-3:position] == "CH2" and input[position+2:position+5] == "CH3"):
        ketone_val = 0
    elif (input[position-3:position] == "CH2" and input[position+2:position+5] == "CH2"):
        ketone_val = 0
    elif (input[position-3:position] == "CH2" and input[position+2:position+4] == "CH"):
        ketone_val = 0
    elif (input[position-3:position] == "CH2" and input[position+2:position+4] == "CC"):
        ketone_val = 0
    elif (input[position-2:position] == "CC" and input[position+2:position+5] == "CH3"):
        ketone_val = 0
    elif (input[position-2:position] == "CC" and input[position+2:position+5] == "CH2"):
        ketone_val = 0
    elif (input[position-2:position] == "CC" and input[position+2:position+4] == "CH"):
        ketone_val = 0
    elif (input[position-2:position] == "CC" and input[position+2:position+4] == "CC"):
        ketone_val = 0
    else:
        ketone_val = 1
    return ketone_val


def amine(input):
    amine_val = 0
    position = input.find("NH2")

    if (input[position-3:position] == "CH3" and input.find("NH2") > 0):
        amine_val = 1
    elif (input[position-3:position] == "CH2" and input.find("NH2") > 0):
        amine_val = 1
    elif (input[position-2:position] == "CH" and input.find("NH2") > 0):
        amine_val = 1
    elif (input[position-1:position] == "C" and input.find("NH2") > 0):
        amine_val = 1
    else:
        amine_val = 0

    return amine_val


def amide(input):
    amide_val = 0
    position = input.find("CONH2")

    if (input[position-3:position] == "CH3" and input.find("CONH2") > 0):
        amide_val = 1
    elif (input[position-3:position] == "CH2" and input.find("CONH2") > 0):
        amide_val = 1
    elif (input[position-2:position] == "CH" and input.find("CONH2") > 0):
        amide_val = 1
    elif (input[position-1:position] == "C" and input.find("CONH2") > 0):
        amide_val = 1
    else:
        amide_val = 0

    return amide_val


def acid_halide(input):
    acid_halide_val = 0
    position = 0
    halide = ""

    if (input.find("COCl") > 0):
        position = input.find("COCl")
        halide = "Cl"
    elif (input.find("COBr") > 0):
        position = input.find("COBr")
        halide = "Br"
    elif (input.find("COI") > 0):
        position = input.find("COI")
        halide = "I"

    if (input[position-3:position] == "CH3" and input.find("CO" + halide) > 0):
        acid_halide_val = 0
    elif (input[position-3:position] == "CH2" and input.find("CO" + halide) > 0):
        acid_halide_val = 0
    elif (input[position-2:position] == "CH" and input.find("CO" + halide) > 0):
        acid_halide_val = 0
    elif (input[position-1:position] == "C" and input.find("CO" + halide) > 0):
        acid_halide_val = 0
    else:
        acid_halide_val = 1
    return acid_halide_val


def alkyl_halide(input):
    alkyl_halide_val = 0
    position = 0
    halide = ""
    set = wrap(input, 3)

    for i in set:
        if (i == "CH3"):
            alkyl_halide_val = 0
        elif(i == "CH2"):
            alkyl_halide_val = 0
        elif(i == "Cl" or i == "Br" or i == "I" or i == "F"):
            alkyl_halide_val = 0
        else:
            alkyl_halide_val = 1
            return alkyl_halide

    return alkyl_halide_val


def alkane_name(input):
    is_alkane = 0
    position = input.find("ane")

    if(position != -1):
        for i in count:
            if (i == input[:position]):
                return build_alkane(count.index(i)+1)
    else:
        return "1"


def build_alkane(input):
    build = []
    alkane_created = ""
    if(input == 1):
        alkane_created = "CH4"
    elif(input == 2):
        alkane_created = "CH3CH3"
    else:
        build.append("CH3")
        for i in range(input-2):
            build.append("CH2")
        build.append("CH3")

        alkane_created = "".join(build)
    return alkane_created

def alkene_name(input):
	position = input.find("ene")

	if(position!=-1):
		for i in count:
			if (i == input[:position]):
				return build_alkene(count.index(i)+1)
	else:
		return "1"

def build_alkene(input):
	build=[]
	alkene_created = ""
	if(input==2):
		alkene_created = "CH2CH2"
	elif(input==3):
		alkene_created = "CH3CHCH2"
	else:
		build.append("CH3")
		for i in range(input-3):
			build.append("CH2")
		build.append("CHCH2")
		alkene_created = "".join(build)
	return alkene_created

def alkyne_name(input):
	position = input.find("yne")

	if(position!=-1):
		for i in count:
			if (i == input[:position]):
				return build_alkyne(count.index(i)+1)
	else:
		return "1"

def build_alkyne(input):
	build=[]
	alkyne_created = ""
	if(input==2):
		alkyne_created = "CHCH"
	elif(input==3):
		alkyne_created = "CH3CHCH"
	else:
		build.append("CH3")
		for i in range(input-3):
			build.append("CH2")
		build.append("CHCH")
		alkyne_created = "".join(build)
	return alkyne_created


def alcohol_name(input):
	position = input.find("anol")

	if(position!=-1):
		for i in count:
			if (i == input[:position]):
				return build_alcohol(count.index(i)+1)
	else:
		return "1"
		
		
def build_alcohol(input):
	build=[]
	alcohol_created = ""
	if(input==1):
		alcohol_created = "CH3OH"
	else:
		build.append("CH3")
		for i in range(input-1):
			build.append("CH2")
		build.append("OH")
		alcohol_created = "".join(build)
	return alcohol_created

def ketone_name(input):
	position = input.find("one")

	if(position!=-1):
		for i in count:
			if (i == input[:position]):
				return build_alkane(count.index(i)+1)
	else:
		return "1"

def build_ketone(input):
	build=[]
	ketone_created = ""
	if(input==3):
		ketone_created = "CH3COCH3"
	else:
		build.append("CH3")
		for i in range(input-3):
			build.append("CH2")
		build.append("COCH3")
		ketone_created = "".join(build)
	return ketone_created

def amine_name(input):
	position = input.find("amine")

	if(position!=-1):
		for i in count:
			if (i == input[:position]):
				return build_amine(count.index(i)+1)
	else:
		return "1"

def build_amine(input):
	build=[]
	amine_created = ""
	if(input==1):
		amine_created = "CH3NH2"
	else:
		build.append("CH3")
		for i in range(input-1):
			build.append("CH2")
		build.append("NH2")
		amine_created = "".join(build)
	return amine_created

def amide_name(input):
	position = input.find("anoic")

	if(position!=-1):
		for i in count:
			if (i == input[:position]):
				return build_amide(count.index(i)+1)
	else:
		return "1"

def build_amide(input):
	build=[]
	amide_created = ""
	if(input==2):
		amide_created = "CH3CHONH2"
	else:
		build.append("CH3")
		for i in range(input-2):
			build.append("CH2")
		build.append("CHONH2")
		amide_created = "".join(build)
	return amide_created

def alkyl_halide_name(input):
	position = input.find("yl")

	if(position!=-1):
		for i in count:
			if (i == input[:position]):
				return build_alkyl_halide(count.index(i)+1,input)
	else:
		return "1"

def build_alkyl_halide(input,molecule):
	build=[]
	alkyl_halide_created = ""

	if(molecule.find("chloride")>0):
		if(input==1):
			alkyl_halide_created = "CH3Cl"
		else:
			build.append("CH3")
			for i in range(input-1):
				build.append("CH2")
			build.append("Cl")
		alkyl_halide_created = "".join(build)
	
	elif(molecule.find("fluoride")>0):
		if(input==1):
			alkyl_halide_created = "CH3F"
		else:
			build.append("CH3")
			for i in range(input-1):
				build.append("CH2")
			build.append("F")
		alkyl_halide_created = "".join(build)

	elif(molecule.find("iodide")>0):
		if(input==1):
			alkyl_halide_created = "CH3I"
		else:
			build.append("CH3")
			for i in range(input-1):
				build.append("CH2")
			build.append("I")
		alkyl_halide_created = "".join(build)

	elif(molecule.find("bromide")>0):
		if(input==1):
			alkyl_halide_created = "CH3Br"
		else:
			build.append("CH3")
			for i in range(input-1):
				build.append("CH2")
			build.append("Br")
		alkyl_halide_created = "".join(build)

	return alkyl_halide_created

def acide_halide_name(input):
	position = input.find("anoyl")

	if(position!=-1):
		for i in count:
			if (i == input[:position]):
				return build_acid_halide(count.index(i)+1,input)
	else:
		return "1"
				
def build_acid_halide(input,molecule):
	build=[]
	acid_halide_created = ""

	if(molecule.find("chloride")>0):
		if(input==1):
			acid_halide_created = "CHOCl"
		else:
			build.append("CH3")
			for i in range(input-2):
				build.append("CH2")
			build.append("COCl")
		acid_halide_created = "".join(build)
	
	elif(molecule.find("fluoride")>0):
		if(input==1):
			acid_halide_created = "CHOF"
		else:
			build.append("CH3")
			for i in range(input-2):
				build.append("CH2")
			build.append("COF")
		acid_halide_created = "".join(build)

	elif(molecule.find("iodide")>0):
		if(input==1):
			acid_halide_created = "CHOI"
		else:
			build.append("CH3")
			for i in range(input-2):
				build.append("CH2")
			build.append("COI")
		acid_halide_created = "".join(build)

	elif(molecule.find("Bromide")>0):
		if(input==1):
			acid_halide_created = "CHOBr"
		else:
			build.append("CH3")
			for i in range(input-2):
				build.append("CH2")
			build.append("COBr")
		acid_halide_created = "".join(build)

	return acid_halide_created