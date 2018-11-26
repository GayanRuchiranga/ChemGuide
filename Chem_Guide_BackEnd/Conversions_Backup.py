from flask import json, jsonify
import textwrap
#import recursion
import identify_molecule


def analyze(input, output):
    final_answer = ""
    carbon = carbon_difference(input, output)

    input_mol = identify_molecule.identify_molecule(input)
    output_mol = identify_molecule.identify_molecule(output)

    print(input_mol)
    print(output_mol)

    if(input_mol == "failed_identification" or output_mol == "failed_identification"):
        return "failed_identification"
    elif input_mol == "alcohol" and output_mol == "alkane" and carbon > 0:
        final_answer = alcoholToAlkane_G(input, output, carbon)
    elif input_mol == "alcohol" and output_mol == "alkane" and carbon == 0:
        final_answer = alcoholToAlkane_E(input, output)
    elif input_mol == "alkyl_halide" and output_mol == "ester" and carbon > 0:
        final_answer = alkyl_halideTocarboxylic_acid(input, output, carbon)
    elif input_mol == "aldehyde" and output_mol == "cyanide"and carbon == 1:
        final_answer = aldehydeTocyanide(input, output, carbon)
    elif input_mol == "carboxylic_acid" and output_mol == "alkyne"and carbon > 0:
        final_answer = carboxylic_acidToalkyne(input, output, carbon)
    return final_answer


def carbon_difference(input1, input2):

    input1_carbon_count = 0
    input2_carbon_count = 0

    for carbon in input1:
        if (carbon == "c" or carbon == "C"):
            input1_carbon_count += 1

    position1 = input1.find("Cl")
    if(position1 > 0):
        input1_carbon_count -= 1

    for carbon in input2:
        if (carbon == "c" or carbon == "C"):
            input2_carbon_count += 1

    position2 = input2.find("Cl")
    if(position2 > 0):
        input2_carbon_count -= 1

    return input2_carbon_count - input1_carbon_count


def carbon_count(input):
    input_carbon_count = 0
    position = input.find("Cl")

    for carbon in input:
        if (carbon == "c" or carbon == "C"):
            input_carbon_count += 1

    if(position > 0):
        input_carbon_count -= 1

    return input_carbon_count


def build_molecule(input):
    chloride = []
    molecule = ""
    if input == 1:
        return "CH3"
    else:
        count = input - 1
        chloride.append("CH3")
        for i in range(count):
            chloride.append("CH2")
    molecule = "".join(chloride)
    return molecule


def alcoholToAlkane_G(input1, input2, input3):

    additional_molecule = ""
    front = ""
    position = input1.find("OH")
    final_output = []

    if position + 2 == len(input1) and input3 > 0:
        additional_molecule = build_molecule(input3)

        front = input1[:position]

        final_output.append(input1)
        final_output.append("PCl3+ Heat OR PCl5+Heat")
        final_output.append(front+"Cl")
        final_output.append("Mg/Dry ether")
        final_output.append(front+"MgCl")
        final_output.append(additional_molecule+"Cl")

        if len(additional_molecule) > 3:
            temp_string = ",".join(textwrap.wrap(additional_molecule, 1))
            temp_array = temp_string.split(",")
            temp_array[:3] = "CH2"
            temp_array[-3:] = "CH3"

            additional_molecule = "".join(temp_array)

        final_output.append(front+additional_molecule)

    return ",".join(final_output)


def alcoholToAlkane_E(input1, input2):
    final_output = []

    if (carbon_count(input1) == 2):
        final_output.append(input1)
        final_output.append("con. H2SO4")
        final_output.append("CH2CH2")
        final_output.append("H2/Ni")
        final_output.append("CH3CH3")
    elif (carbon_count(input1) > 2):
        position = input1.find("OH")
        # R-OH format
        if(position+2 == len(input1)):
            final_output.append(input1)
            final_output.append("con. H2SO4")
            final_output.append(
                input1[:position-4]+input1[position-3:position])
            final_output.append("H2/Ni")
            final_output.append(input1[:position][:-3]+"CH3")
        else:
            # R-OH-R format
            pos1 = input1.find("OHCH3")
            pos2 = input1.find("OHCH2")
            # R-OH-CH3 format
            if(pos1 > 0):
                final_output.append(input1)
                final_output.append("con. H2SO4")
                final_output.append(input1[:pos1]+"CH2")
                final_output.append("H2/Ni")
                final_output.append(input1[:pos1-2]+"CH2CH3")

            # R-OH-CH2-R format
            elif(pos2 > 0):
                rest = input1[pos2+5:]
                final_output.append(input1)
                final_output.append("con. H2SO4")
                final_output.append(input1[:pos2]+"CH"+rest)
                final_output.append("H2/Ni")
                final_output.append(input1[:pos2-2]+"CH2CH2"+rest)
    return ",".join(final_output)


def alkyl_halideTocarboxylic_acid(input1, input2, input3):
    additional_molecule = ""
    front = ""
    final_output = []
    position = input1.find("Cl")

    if position + 2 == len(input1) and input3 > 0:
        additional_molecule = build_molecule(input3)
        front = input1[:position]

        final_output.append(input1)
        final_output.append("NaOH(aq)")
        final_output.append(front+"OH")
        final_output.append("H+/KMnO4")
        final_output.append(front[:-3]+"COOH")
        final_output.append(additional_molecule+"OH/con.H2SO4")

        if len(additional_molecule) > 3:
            temp_string = ",".join(textwrap.wrap(additional_molecule, 1))
            temp_array = temp_string.split(",")
            temp_array[:3] = "CH2"
            temp_array[-3:] = "CH3"

            additional_molecule = "".join(temp_array)

        final_output.append(front[:-3]+"COO"+additional_molecule)
        print(final_output)
    return ",".join(final_output)


def aldehydeTocyanide(input1, input2, input3):
    front = ""
    final_output = []
    position = input1.find("COH")

    front = input1[:position]

    final_output.append(input1)
    final_output.append("H+/KMnO4")
    final_output.append(front+"COOH")
    final_output.append("PCl3/PCl5 SOCl2")
    final_output.append(front+"COCl")
    final_output.append("NH3")
    final_output.append(front+"CONH2")
    final_output.append("LiAlH4")
    final_output.append(front+"CH2NH2")
    final_output.append("con.KOH/CHCl3/70c")
    final_output.append(front+"CH2CN")

    return ",".join(final_output)


def carboxylic_acidToalkyne(input1, input2, input3):
    additional_molecule = ""
    front = ""
    final_output = []
    position = input1.find("COOH")
    additional_molecule = build_molecule(input3)
    front = input1[:position]

    final_output.append(input1)
    final_output.append("LiAlH4")
    final_output.append(front+"CH2OH")
    final_output.append("PBr3")
    final_output.append(front+"CH2Br")
    final_output.append("Mg/Dry ether")
    final_output.append(front+"CH2MgBr")
    final_output.append(additional_molecule[:-2]+"OH/H2O")

    if len(additional_molecule) > 3:
        temp_string = ",".join(textwrap.wrap(additional_molecule, 1))
        temp_array = temp_string.split(",")
        temp_array[:3] = "CH2"
        temp_array[-3:] = "CH3"

        additional_molecule = "".join(temp_array)
    final_output.append(front+"CHOH"+additional_molecule)
    final_output.append("con. H2SO4")
    final_output.append(front+"CHCH"+additional_molecule[3:])
    final_output.append("Br2/CCl4")
    final_output.append(front+"CHBrCHBr"+additional_molecule[3:])
    final_output.append("Alc KOH")
    final_output.append(front+"CC"+additional_molecule[3:])
    return ",".join(final_output)
