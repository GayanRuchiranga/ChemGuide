from flask import json, jsonify
import identify_molecule

data = '{"alkane": [{"in": "CH3CH2CH3", "put": "hv/Cl2", "out": "CH3CH(Cl)CH3"}],"alkene": [{"in": "CH3CHCH2", "put": "OH-/KMnO4", "out": "CH2CH(OH)+CH2OH"},{"in": "CH3CHCH2", "put": "dil. H2SO4", "out": "CH3CHOHCH3"},{"in": "CH3CHCH2", "put": "2H2/Pt,Pd/Ni", "out": "CH3CH2CH3"},{"in": "CH3CHCH2", "put": "HBr", "out": "CH3CHBrCH3"},{"in": "CH3CHCH2", "put": "Br2/CCl4", "out": "CH3CHBrCH2Br"},{"in": "CH3CHCH2", "put": "H2/Pt", "out": "CH3CH2CH3"}],"alkyne": [{"in": "CH3CCH", "put": "OH-/KMnO4", "out": "CH3COCOH"},{"in": "CH3CCH", "put": "2H2/Ni", "out": "CH3CH2CH3"},{"in": "CH3CCH", "put": "Hg2+/con. H2SO4/60c", "out": "CH3COCH3"},{"in": "CH3CCH", "put": "Br2/CCl4", "out": "CH3CBr2CHBr2"},{"in": "CH3CCH", "put": "HBr", "out": "CH3CBr2CH3"},{"in": "CH3CCH", "put": "H2/Pd BaSO4 Quinoline", "out": "CH3CHCH2"},{"in": "CH3CCH", "put": "NaNH2 Na/NH3", "out": "CH3CC-Na+"},{"in": "CH3CCH", "put": "[Ag(NH3)2]+ Tollens", "out": "CH3CCAg(s) White"},{"in": "CH3CCH", "put": "Cu2Cl2/NH3", "out": "CH3CCCu(s) Red"}],"alkyl_halide": [{"in": "CH3CH(Cl)CH3", "put": "Alc KOH", "out": "CH3CHCH2"},{"in": "CH3CH(Cl)CH3", "put": "Mg/Dry ether", "out": "CH3CH(MgCl)CH3"},{"in": "CH3CH(Cl)CH3", "put": "Mg/Dry ether H+/H2O", "out": "CH3CH2CH3"},{"in": "CH3CH(Cl)CH3", "put": "NH3", "out": "CH3CH(NH2)CH3"},{"in": "CH3CH(Cl)CH3", "put": "CH3MgCl", "out": "CH3CH(CH3)CH3"},{"in": "CH3CH(Cl)CH3", "put": "Aq/Alc KCN", "out": "CH3CH(CN)CH3"},{"in": "CH3CH2Cl", "put": "NaOH(aq)", "out": "CH3CH2OH"}],"alcohol": [{"in": "CH3CH2OH", "put": "Na", "out": "CH3CH2O-Na+"},{"in": "CH3CH2OH", "put": "CH3COCl", "out": "CH3COOCH2CH3"},{"in": "CH3CH2OH", "put": "CH3COOH", "out": "CH3COOCH2CH3"},{"in": "CH3CH2OH", "put": "PCl3/PCl5 SOCl2", "out": "CH3CH2Cl"},{"in": "CH3CH2OH", "put": "HBr", "out": "CH3CH2Br"},{"in": "CH3CH2OH", "put": "ZnCl2/con.HCl", "out": "CH3CH2Cl"},{"in": "CH3CH2OH", "put": "H+/KMnO4", "out": "CH3COOH"},{"in": "CH3CHOHCH3", "put": "con.H2SO4 Al2O3/350c", "out": "CH3CHCH2"}],"aldehyde": [{"in": "CH3COH", "put": "HCN", "out": "CH3CHCNOH"},{"in": "CH3COH", "put": "CH3CH2MgCl", "out": "CH3CHOHCH2CH3"},{"in": "CH3COH", "put": "NaOH", "out": "CH3CHOHCH2CHO"},{"in": "CH3COH", "put": "NaOH/I2", "out": "CHI3(s) Yellow"},{"in": "CH3COH", "put": "faling", "out": "CH3COO- + Cu2O(s)"},{"in": "CH3COH", "put": "Tollens", "out": "CH3COO- + Ag(s)"},{"in": "CH3COH", "put": "H+/KMnO4", "out": "CH3COOH"},{"in": "CH3COH", "put": "Zn[Hg] con.HCl", "out": "CH3CH3"},{"in": "CH3COH", "put": "LiAlH4", "out": "CH3CH2OH"},{"in": "CH3COH", "put": "CH3NHCH3", "out": "CH2CHNCH3"},{"in": "CH3COH", "put": "CH3NH2", "out": "CH3NCHCH3"}],"ketone": [{"in": "CH3COCH3", "put": "HCN", "out": "CH3C(CN)(OH)CH3"},{"in": "CH3COCH3", "put": "CH3CH2MgCl/H2O", "out": "CH3C(OH)(OH)CH2CH3"},{"in": "CH3COCH3", "put": "NaOH", "out": "CH3C(OH)(CH3)CH2COCH3"},{"in": "CH3COCH3", "put": "NaOH/I2", "out": "CHI3(s) Yellow"},{"in": "CH3COCH3", "put": "Zn[Hg] con.HCl", "out": "CH3CH2CH3"},{"in": "CH3COCH3", "put": "LiAlH4", "out": "CH3CH(CH3)OH"},{"in": "CH3COCH3", "put": "CH3NHCH3", "out": "CH3C(CH3)N(CH3)CH3"},{"in": "CH3COCH3", "put": "CH3NH2", "out": "CH3C(CH3)NCH3"}],"carboxylic_acid": [{"in": "CH3COOH", "put": "LiAlH4", "out": "CH3CH2OH"},{"in": "CH3COOH", "put": "Na2CO3", "out": "CH3COO-Na+ + H2O + CO2"},{"in": "CH3COOH", "put": "PCl3/PCl5 SOCl2", "out": "CH3COCl"},{"in": "CH3COOH", "put": "NaOH", "out": "CH3COO-Na+ + H2O"},{"in": "CH3COOH", "put": "Na", "out": "CH3COO-Na+ + H2(g)"}],"carboxylic_acid_chloride": [{"in": "CH3CH2COCl", "put": "CH3NH2", "out": "CH3CH2CONHCH3"},{"in": "CH3CH2COCl", "put": "CH3OH", "out": "CH3CH2COOCH3"},{"in": "CH3CH2COCl", "put": "NH3", "out": "CH3CH2CONH2"},{"in": "CH3CH2COCl", "put": "CH3MgCl(2 mol)/H2O", "out": "CH3CH2C(CH3)(OH)CH3"}],"ester": [{"in": "CH3COOCH3", "put": "H+/H2O", "out": "CH3COOH + CH3OH"},{"in": "CH3COOCH3", "put": "NaOH", "out": "CH3COO-Na+ + CH3OH"},{"in": "CH3COOCH3", "put": "NH3/Heat", "out": "CH3CONH2 + CH3OH"},{"in": "CH3COOCH3", "put": "LiAlH4/H2O", "out": "CH3CH2OH + CH3OH"},{"in": "CH3COOCH3", "put": "CaO(s)/NaOH(s)", "out": "CH4"},{"in": "CH3COOCH3", "put": "dil.H2SO4", "out": "CH3COOH + CH3OH"}],"amide": [{"in": "CH3CONH2", "put": "LiAlH4", "out": "CH3CH2NH2"},{"in": "CH3CONH2", "put": "NaOH/Heat", "out": "CH3COO-Na+ + NH3(g)"}],"amine": [{"in": "CH3CH2NH2", "put": "CH3COCl", "out": "CH3CH2NHCOCH3"},{"in": "CH3CH2NH2", "put": "NaNO2/HCl (HNO2)", "out": "CH3CH2OH"},{"in": "CH3CH2NH2", "put": "CH3Cl", "out": "CH2CH2NHCH3"},{"in": "CH3CH2NH2", "put": "con.KOH CHCL3/70c", "out": "CH3CH2NC"},{"in": "CH3CH2NH2", "put": "CH3CHO", "out": "CH3CH2NCHCH3"},{"in": "CH3CH2NH2", "put": "CH3Cl(2 mol)/Heat", "out": "CH3CH2N(CH3)2"}]}'


def analyze(input, output):
    # Identify the input molecule
    input_mol = identify_molecule.identify_molecule(input)
    # Identify the output molecule
    output_mol = identify_molecule.identify_molecule(output)

    if(input_mol == "failed_identification" or output_mol == "failed_identification"):
        return "failed_identification"
    else:
        print(first_iteration(input, input_mol, output, output_mol))
        json_obj = json.loads(data)
    return json_obj[input_mol]+json_obj[output_mol]


def first_iteration(input, input_mol, output, output_mol):
    steps = []
    json_obj = json.loads(data)
    input_category_data = json_obj[input_mol]

    for i in range(len(input_category_data)):
        if(identify_molecule.identify_molecule(input_category_data[i]["out"]) == output_mol):
            print("Found")
            steps.append(input_category_data[i]["in"])
            steps.append(input_category_data[i]["put"])
            steps.append(input_category_data[i]["out"])
        else:
            print("failed_not_found")

    if(len(steps) > 0):
        return ",".join(steps)
    else:
        return "1"
