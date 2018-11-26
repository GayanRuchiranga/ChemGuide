import pandas as data_reader
import warnings
warnings.filterwarnings('ignore')
date_set= data_reader.read_csv('data_training.csv', encoding = "ISO-8859-1")

def analyze(textt):
    
    #text = 'X and Y are s block elements of the Periodic Table. They react with water to form hydroxides. The hydroxide of X is more basic than that of Y. The hydrocide of X is used in the manufacture of baby soap. The hydroxide of Y is commonly used to identify the gas Z that is one of the main gases responsible for global warming. A belongs to the S block. B is a element of P block. The hydrocide of C is used in the manufacture of kraft. The hydroxide of D is commonly used to identify the liquid Fe2+. M reacts with N and form the gas H2S. E reacts with P and form the solid Al(OH)3. Q reacts with R and form the solution NaCl. S reacts with T and form the gas HI. When heating the compound U it makes the MgO. When doing the flame test to the Compound V it forms a pale-green color flame. An element W, belongs to the P block.'

    fulllength=len(date_set.index)
    sentence= (textt.split(". "))
    sentencelen=len(sentence)
    final_output=[]

    for k in range (sentencelen):

        sentence0=(sentence[k].split(" "))
        sentence0[len(sentence0)-1]=sentence0[len(sentence0)-1].replace(".","")

        for m in range(len(date_set.index)):
            

            samplelength =date_set.loc[m,'length']
            sentencelength=len(sentence0)

            count = 0
            i = 0
            if samplelength == sentencelength:

                #sample=date_set.loc[0,'sample']
                sample0=(date_set.loc[m,'sample'].split(" "))



                while i < sentencelength:
                    if sentence0[i]!=sample0[i]:

                        count= count+1



                    i += 1

            else:
                i += 1

            indx=0

            if count == date_set.loc[m,'hintcount']:
                indx = m

                            
            if indx == 8:
            
                if sentence0[4] == "S" or sentence0[4] =="s":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"Selements"]) != True:
                        
                            array.append(date_set.loc[cnt,"Selements"])
                        
                            hydro=date_set.loc[cnt,"Selements"]
                    
                    
                    final_output.append(sentence0[0]+" and "+sentence0[2]+" might be "+" ".join(array))
                    
                    
                if sentence0[4] == "P" or sentence0[4] =="p":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"Pelements"]) != True:
                            
                            array.append(date_set.loc[cnt,"Pelements"])
                    
                    
                    final_output.append(sentence0[0]+" and "+sentence0[2]+" might be "+" ".join(array))
                    
                if sentence0[4] == "D" or sentence0[4] =="d":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"Delements"]) != True:
                            
                            array.append(date_set.loc[cnt,"Delements"])
                    
                    
                    final_output.append(sentence0[0]+" and "+sentence0[2]+" might be "+" ".join(array))

            if indx == 9:
                if sentence0[3] == "water" and sentence0[6] =="hydroxides":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"hydroxide"]) != True:
                            
                        
                            if date_set.loc[cnt,"hydroxide"] != 'n_a':
                            
                                array.append(date_set.loc[cnt,"hydroxide"])
                        
                            
                        
                        #final_output.append("Hydroxides are "+hydro)
                        
                    final_output.append("Hydroxides are "+" ".join(array))


            if indx == 10:
        
                array=[]        
                if sentence0[5] == "more":
                    
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"hydroxide"]) != True:
                        
                            if date_set.loc[cnt,"hydroxide"] != 'n_a':
                                
                                array.append(date_set.loc[cnt,"hydroxide"])
                            
                    final_output.append("Ascending order "+" ".join(array))
                    
                        
                if sentence0[5] == "less":
                    
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"hydroxide"]) != True:
                        
                            if date_set.loc[cnt,"hydroxide"] != 'n_a':
                            
                                array.append(date_set.loc[cnt,"hydroxide"])
                            
                    final_output.append("Descending order "+" ".join(list(reversed(array))))

            if indx == 11:
        
                array=[]
                
                if sentence0[5] == "used" and sentence0[8] =="manufacture":
                    
                    for cnt in range (fulllength):
                        
                        if sentence0[10]==date_set.loc[cnt,"used"]:
                            
                            array.append(date_set.loc[cnt,"used"])
                    
                    
                    if len(array) == 1:
                        
                        for cnt in range (fulllength):
                            if array[0]==date_set.loc[cnt,"used"]:
                                final_output.append(sentence0[3]+" is "+ date_set.loc[cnt,"Selements"])

            if indx == 12:
        
                array=[]
                    
                if sentence0[6] == "used" and sentence0[8] =="identify": 
                    
                    for cnt in range (fulllength):
                        
                        if sentence0[10]==date_set.loc[cnt,"state"]:
                            
                            array.append(date_set.loc[cnt,"identify"])
                            
                    #final_output.append(" ".join(array))
                        
                    if len(array) == 1:
                        
                        for cnt in range (fulllength):
                            if array[0]==date_set.loc[cnt,"identify"]:
                                
                                final_output.append(sentence0[11]+" is "+ date_set.loc[cnt,"identify"])
                                final_output.append(sentence0[3]+" is "+ date_set.loc[cnt,"Selements"])

            if indx == 13:
            
                if sentence0[4] == "S" or sentence0[4] =="s":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"Selements"]) != True:
                        
                            array.append(date_set.loc[cnt,"Selements"])
                    
                    
                    final_output.append(sentence0[0]+" might be "+" ".join(array))
                    
                if sentence0[4] == "P" or sentence0[4] =="p":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"Pelements"]) != True:
                        
                            array.append(date_set.loc[cnt,"Pelements"])
                    
                    
                    final_output.append(sentence0[0]+" might be "+" ".join(array))
                    
                if sentence0[4] == "D" or sentence0[4] =="d":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"Delements"]) != True:
                        
                            array.append(date_set.loc[cnt,"Delements"])
                    
                    
                    final_output.append(sentence0[0]+" might be "+" ".join(array))


            if indx == 14:
            
                if sentence0[5] == "S" or sentence0[5] =="s":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"Selements"]) != True:
                        
                            array.append(date_set.loc[cnt,"Selements"])
                    
                    
                    final_output.append(sentence0[0]+" might be "+" ".join(array))
                    
                if sentence0[5] == "P" or sentence0[5] =="p":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"Pelements"]) != True:
                        
                            array.append(date_set.loc[cnt,"Pelements"])
                    
                    
                    final_output.append(sentence0[0]+" might be "+" ".join(array))
                    
                if sentence0[5] == "D" or sentence0[5] =="d":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"Delements"]) != True:
                        
                            array.append(date_set.loc[cnt,"Delements"])
                    
                    
                    final_output.append(sentence0[0]+" might be "+" ".join(array))

            if indx == 18:
        
                array=[]
                
                if sentence0[5] == "used" and sentence0[8] =="manufacture":
                    
                    for cnt in range (fulllength):
                        
                        if sentence0[10]==date_set.loc[cnt,"used"]:
                            
                            array.append(date_set.loc[cnt,"used"])
                            
                    #final_output.append(" ".join(array))
                    
                    if len(array) == 1:
                        
                        for cnt in range (fulllength):
                            if array[0]==date_set.loc[cnt,"used"]:
                                final_output.append(sentence0[3]+" is "+ date_set.loc[cnt,"Selements"])

            if indx == 19:
        
                array=[]
                    
                if sentence0[6] == "used" and sentence0[8] =="identify": 
                    
                    for cnt in range (fulllength):
                        
                        if sentence0[10]==date_set.loc[cnt,"state"]:
                            
                            array.append(date_set.loc[cnt,"identify"])
                            
                    final_output.append(" ".join(array))
                        
                    if len(array) == 1:
                        
                        for cnt in range (fulllength):
                            if array[0]==date_set.loc[cnt,"identify"]:
                                
                                final_output.append(sentence0[11]+" is "+ date_set.loc[cnt,"identify"])
                                final_output.append(sentence0[3]+" is "+ date_set.loc[cnt,"Selements"])

            if indx == 20:
                if sentence0[7] == "solid":
                    
                    for cnt in range (len(date_set.index)):
                        
                        if sentence0[8]==date_set.loc[cnt,"solid"]:
                            
                            final_output.append(sentence0[0]+" or "+sentence0[3]+" should be "+date_set.loc[cnt,"first"]+" and "+date_set.loc[cnt,"second"])
                
                if sentence0[7] == "solution":
                    
                    for cnt in range (len(date_set.index)):
                        
                        if sentence0[8]==date_set.loc[cnt,"solution"]:
                            
                            final_output.append(sentence0[0]+" or "+sentence0[3]+" should be "+date_set.loc[cnt,"first"]+" and "+date_set.loc[cnt,"second"])
                        
                if sentence0[7] == "gas":
                    
                    for cnt in range (len(date_set.index)):
                        
                        if sentence0[8]==date_set.loc[cnt,"gas"]:
                            
                            final_output.append(sentence0[0]+" or "+sentence0[3]+" should be "+date_set.loc[cnt,"first"]+" and "+date_set.loc[cnt,"second"])
                        
            if indx == 24:
                
                for cnt in range (fulllength):
                        
                    if sentence0[8] == date_set.loc[cnt,"solid"] and sentence0[11] == date_set.loc[cnt,"solution"]:
                                    
                        if data_reader.isnull(date_set.loc[cnt,"solution"]) != True:
                            
                            final_output.append(sentence0[0]+" and "+sentence0[3]+" might be "+date_set.loc[cnt,"first"]+" and "+date_set.loc[cnt,"second"])

            if indx == 25:
                
                for cnt in range (fulllength):
                        
                    if sentence0[8] == date_set.loc[cnt,"solution"] and sentence0[11] == date_set.loc[cnt,"gas"]:
                                    
                        if data_reader.isnull(date_set.loc[cnt,"solution"]) != True:
                            
                            final_output.append(sentence0[0]+" and "+sentence0[3]+" might be "+date_set.loc[cnt,"first"]+" and "+date_set.loc[cnt,"second"])
                        
             
            if indx == 26:
                for cnt in range (len(date_set.index)):
                    
                                    
                    if sentence0[8]==date_set.loc[cnt,"heated"]:
                            
                        final_output.append(sentence0[4]+" is "+date_set.loc[cnt,"first"] ) 

            if indx == 27:
                for cnt in range (len(date_set.index)):
                        
                        if sentence0[12]==date_set.loc[cnt,"flame"]:
                            
                            final_output.append(sentence0[8]+" is "+date_set.loc[cnt,"first"] )

            if indx == 28:
        
                for cnt in range (fulllength):
                        
                    if sentence0[11] == date_set.loc[cnt,"sulfides"]:
                        
                        if data_reader.isnull(date_set.loc[cnt,"sulfides"]) != True:
                            
                            final_output.append(sentence0[6]+" should be "+date_set.loc[cnt,"first"])                

            if indx == 29:
            
                if sentence0[6] == "S" or sentence0[6] =="s":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"Selements"]) != True:
                            
                            array.append(date_set.loc[cnt,"Selements"])
                    
                    
                    final_output.append(sentence0[2].replace(",","")+" might be "+" ".join(array))
                    
                if sentence0[6] == "P" or sentence0[6] =="p":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"Pelements"]) != True:
                            
                            array.append(date_set.loc[cnt,"Pelements"])
                    
                    
                    final_output.append(sentence0[2].replace(",","")+" might be "+" ".join(array))
                    
                if sentence0[6] == "D" or sentence0[6] =="d":
                    array=[]
                    for cnt in range (fulllength):
                        
                        if data_reader.isnull(date_set.loc[cnt,"Delements"]) != True:
                            
                            array.append(date_set.loc[cnt,"Delements"])
                    
                    
                    final_output.append(sentence0[2].replace(",","")+" might be "+" ".join(array))

            if indx == 18:
        
                array=[]
                
                if sentence0[2] == "used" and sentence0[5] =="manufacture":
                    
                    for cnt in range (fulllength):
                        
                        if sentence0[7]==date_set.loc[cnt,"manufacture"]:
                            
                            array.append(date_set.loc[cnt,"manufacture"])
                            
                    #final_output.append(" ".join(array))
                    
                    if len(array) == 1:
                        
                        for cnt in range (fulllength):
                            if array[0]==date_set.loc[cnt,"manufacture"]:
                                final_output.append(sentence0[0]+" is "+ date_set.loc[cnt,"manufacture"])

    final=", ".join(final_output)
    
    return_Output=[]

    return_Output.append(textt+"975"+final)

    return textt+"975"+final