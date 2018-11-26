from textwrap import wrap


# function to identify the molecule


def identify_molecule(input):
    if(int(alkane(input)) == 0):
        return "alkane"
    elif(int(alkene(input)) == 0):
        return "alkene"
    elif(int(alkyne(input)) == 0):
        return "alkyne"
    elif(int(alkyl_halide(input)) == 0):
        return "alkyl_halide"
    elif(int(alcohol(input)) == 0):
        return "alcohol"
    elif(int(aldehyde(input)) == 0):
        return "aldehyde"
    elif(int(ketone(input)) == 0):
        return "ketone"
    elif(int(carbo_acid(input)) == 0):
        return "carboxylic_acid"
    elif(int(acid_halide(input)) == 0):
        return "carboxylic_acid_chloride"
    elif(int(ester(input)) == 0):
        return "ester"
    elif(int(amide(input)) == 0):
        return "amide"
    elif(int(amine(input)) == 0):
        return "amine"
    elif(int(cyanide(input))==0):
        return "cyanide"
    elif(int(sodium_salt(input))==0):
        return "sodium_salt"
    else:
        return "failed_identification"

# Identify Alkane


def alkane(input):
    carbon = 0
    hydrogen = 0
    alkane_val = 0

    for i in input:
        if i == "C" or i == "c":
            carbon += 1
        elif i == "H" or i == "h":
            hydrogen += 1
        elif i.isdigit():
            hydrogen += int(i)-1
        else:
            alkane_val = 1

    if alkane_val != 1 and hydrogen == ((carbon * 2)+2):
        return "0"
    else:
        return "1"


# Identify Alkene


def alkene(input):
    carbon = 0
    hydrogen = 0
    alkene_val = 0

    for i in input:
        if i == "C" or i == "c":
            carbon += 1
        elif i == "H" or i == "h":
            hydrogen += 1
        elif i.isdigit():
            hydrogen += int(i)-1
        else:
            alkene_val = 1

    if alkene_val != 1 and hydrogen == ((carbon * 2)):
        return "0"
    else:
        return "1"


# Identify Alkyne


def alkyne(input):
    carbon = 0
    hydrogen = 0
    alkyne_val = 0

    for i in input:
        if i == "C" or i == "c":
            carbon += 1
        elif i == "H" or i == "h":
            hydrogen += 1
        elif i.isdigit():
            hydrogen += int(i)-1
        else:
            alkyne_val = 1

    if(input == "CHCH"):
        return "0"
    elif alkyne_val != 1 and hydrogen == ((carbon * 2)-2):
        return "0"
    else:
        return "1"


# Identify Alkyl Halide
def alkyl_halide(input):
    alkyl_halide_val = 0
    position = input.find("Cl")
    if(position > 0):
        split_arr = wrap(input, 3)
        for i in split_arr:
            if (i == "CH3"):
                alkyl_halide_val = 0
                # print(i)
            elif(i == "CH2"):
                # print(i)
                alkyl_halide_val = 0
            elif(i == "Cl" or i == "Br" or i == "I" or i == "F"):
                # print(i)
                alkyl_halide_val = 0
            else:
                alkyl_halide_val = 1
                return alkyl_halide_val
    else:
        alkyl_halide_val = 1
    return alkyl_halide_val

# Identify alcohol


def alcohol(input):
    carbon = 0
    hydrogen = 0
    oxygen = 0
    alcohol_val = 0
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
            alcohol_val = 1

    if alcohol_val != 1 and hydrogen == ((carbon * 2)+2) and oxygen == 1:
        # return 0 if it is an alcohol
        return "0"
    else:
        # return 1 if it is not an alcohol
        return "1"

# identify Aldehyde


def aldehyde(input):
    aldehyde_val = 0

    if input == "CHOH":
        aldehyde_val = 0
    elif (input.find("COH") == -1):
        aldehyde_val = 1
    return aldehyde_val


# Identify Ketone


def ketone(input):
    ketone_val = 0

    position = input.find("CO")
    if(ester(input) > 0 and position > 0):
        ketone_val = 0
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


# Identify Carboxylic Acid


def carbo_acid(input):
    carbo_acid_val = 0

    if (input.find("COOH") == -1):
        carbo_acid_val = 1
    else:
        carbo_acid_val = 0
    return carbo_acid_val


# Identify Acide Halide


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

    if (input.find("CO" + halide) > 0 and input[position-3:position] == "CH3"):
        acid_halide_val = 0
    elif (input.find("CO" + halide) > 0 and input[position-3:position] == "CH2"):
        acid_halide_val = 0
    elif (input.find("CO" + halide) > 0 and input[position-2:position] == "CH"):
        acid_halide_val = 0
    elif (input.find("CO" + halide) > 0 and input[position-1:position] == "C"):
        acid_halide_val = 0
    else:
        acid_halide_val = 1
    return acid_halide_val


# Identify Ester

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


# Identify Amide

def amide(input):
    amide_val = 0
    position = input.find("CONH2")

    if (position > 0 and input[position-3:position] == "CH3"):
        amide_val = 0
    elif (position > 0 and input[position-3:position] == "CH2"):
        amide_val = 0
    elif (position > 0 and input[position-2:position] == "CH"):
        amide_val = 0
    elif (position > 0 and input[position-1:position] == "C"):
        amide_val = 0
    else:
        amide_val = 1

    return amide_val


# Identify Amine


def amine(input):
    amine_val = 0
    position = input.find("NH2")

    if (position > 0 and input[position-3:position] == "CH3"):
        amine_val = 0
    elif (position > 0 and input[position-3:position] == "CH2"):
        amine_val = 0
    elif (position > 0 and input[position-2:position] == "CH"):
        amine_val = 0
    elif (position > 0 and input[position-1:position] == "C"):
        amine_val = 0
    else:
        amine_val = 1

    return amine_val

def cyanide(input):
    carbon = 0
    hydrogen = 0
    nitrogen =0
    cyanide_val = 0

    for i in input:
        if i == "C" or i == "c":
            carbon += 1
        elif i == "H" or i == "h":
            hydrogen += 1
        elif i.isdigit():
            hydrogen += int(i)-1
        elif i=="N" or i=="n":
            nitrogen += 1
        else:
            cyanide_val = 1

    if cyanide_val != 1 and hydrogen == ((carbon * 2)-1) and nitrogen==1:
        return "0"
    else:
        return "1"

def sodium_salt(input):
	sodium_salt_val = 0
	
	salt_arr = input.split(" ")
	s_salt = salt_arr[0]
	position = s_salt.find("COO-Na+")
	
	if(position>0):
		sodium_salt_val = 0
	else:
		sodium_salt_val = 1
	return sodium_salt_val