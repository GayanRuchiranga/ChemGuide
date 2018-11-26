#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df= pd.read_csv('data_training.csv', encoding = "ISO-8859-1")


text = 'X and Y are s block elements of the Periodic Table. They react with water to form hydroxides. The hydroxide of X is more basic than that of Y. The hydrocide of X is used in the manufacture of baby soap. The hydroxide of Y is commonly used to identify the gas Z that is one of the main gases responsible for global warming. A belongs to the S block. B is a element of P block. The hydrocide of C is used in the manufacture of kraft. The hydroxide of D is commonly used to identify the liquid Fe2+. M reacts with N and form the gas H2S. E reacts with P and form the solid Al(OH)3. Q reacts with R and form the solution NaCl. S reacts with T and form the gas HI. When heating the compound U it makes the MgO. When doing the flame test to the Compound V it forms a pale-green color flame. An element W, belongs to the P block.'

fulllength=len(df.index)
sentence= (text.split(". "))
sentencelen=len(sentence)
final_output=[]

for k in range (sentencelen):

    sentence0=(sentence[k].split(" "))
    sentence0[len(sentence0)-1]=sentence0[len(sentence0)-1].replace(".","")

    for m in range(len(df.index)):
        

        samplelength =df.loc[m,'length']
        sentencelength=len(sentence0)

        count = 0
        i = 0
        if samplelength == sentencelength:

            #sample=df.loc[0,'sample']
            sample0=(df.loc[m,'sample'].split(" "))



            while i < sentencelength:
                if sentence0[i]!=sample0[i]:

                    count= count+1



                i += 1

        else:
            i += 1

        indx=0

        if count == df.loc[m,'hintcount']:
            indx = m
            
                        
        if indx == 8:
        
            if sentence0[4] == "S" or sentence0[4] =="s":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"Selements"]) != True:
                    
                        array.append(df.loc[cnt,"Selements"])
                    
                        hydro=df.loc[cnt,"Selements"]
                
                
                print(sentence0[0]+" and "+sentence0[2]+" might be "+" ".join(array))
                
            if sentence0[4] == "P" or sentence0[4] =="p":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"Pelements"]) != True:
                        
                        array.append(df.loc[cnt,"Pelements"])
                
                
                print(sentence0[0]+" and "+sentence0[2]+" might be "+" ".join(array))
                
            if sentence0[4] == "D" or sentence0[4] =="d":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"Delements"]) != True:
                        
                        array.append(df.loc[cnt,"Delements"])
                
                
                print(sentence0[0]+" and "+sentence0[2]+" might be "+" ".join(array))

        if indx == 9:
            if sentence0[3] == "water" and sentence0[6] =="hydroxides":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"hydroxide"]) != True:
                        
                    
                        if df.loc[cnt,"hydroxide"] != 'n_a':
                        
                            array.append(df.loc[cnt,"hydroxide"])
                    
                        
                    
                    #print("Hydroxides are "+hydro)
                    
                print("Hydroxides are "+" ".join(array))


        if indx == 10:
    
            array=[]        
            if sentence0[5] == "more":
                
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"hydroxide"]) != True:
                    
                        if df.loc[cnt,"hydroxide"] != 'n_a':
                            
                            array.append(df.loc[cnt,"hydroxide"])
                        
                print(" ".join(array))
                
                    
            if sentence0[5] == "less":
                
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"hydroxide"]) != True:
                    
                        if df.loc[cnt,"hydroxide"] != 'n_a':
                        
                            array.append(df.loc[cnt,"hydroxide"])
                        
                print(" ".join(list(reversed(array))))

        if indx == 11:
    
            array=[]
            
            if sentence0[5] == "used" and sentence0[8] =="manufacture":
                
                for cnt in range (fulllength):
                    
                    if sentence0[10]==df.loc[cnt,"used"]:
                        
                        array.append(df.loc[cnt,"used"])
                        
                print(" ".join(array))
                
                if len(array) == 1:
                    
                    for cnt in range (fulllength):
                        if array[0]==df.loc[cnt,"used"]:
                            print(sentence0[3]+" is "+ df.loc[cnt,"Selements"])

        if indx == 12:
    
            array=[]
                
            if sentence0[6] == "used" and sentence0[8] =="identify": 
                
                for cnt in range (fulllength):
                    
                    if sentence0[10]==df.loc[cnt,"state"]:
                        
                        array.append(df.loc[cnt,"identify"])
                        
                print(" ".join(array))
                    
                if len(array) == 1:
                    
                    for cnt in range (fulllength):
                        if array[0]==df.loc[cnt,"identify"]:
                            
                            print(sentence0[11]+" is "+ df.loc[cnt,"identify"])
                            print(sentence0[3]+" is "+ df.loc[cnt,"Selements"])

        if indx == 13:
        
            if sentence0[4] == "S" or sentence0[4] =="s":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"Selements"]) != True:
                    
                        array.append(df.loc[cnt,"Selements"])
                
                
                print(sentence0[0]+" might be "+" ".join(array))
                
            if sentence0[4] == "P" or sentence0[4] =="p":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"Pelements"]) != True:
                    
                        array.append(df.loc[cnt,"Pelements"])
                
                
                print(sentence0[0]+" might be "+" ".join(array))
                
            if sentence0[4] == "D" or sentence0[4] =="d":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"Delements"]) != True:
                    
                        array.append(df.loc[cnt,"Delements"])
                
                
                print(sentence0[0]+" might be "+" ".join(array))


        if indx == 14:
        
            if sentence0[5] == "S" or sentence0[5] =="s":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"Selements"]) != True:
                    
                        array.append(df.loc[cnt,"Selements"])
                
                
                print(sentence0[0]+" might be "+" ".join(array))
                
            if sentence0[5] == "P" or sentence0[5] =="p":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"Pelements"]) != True:
                    
                        array.append(df.loc[cnt,"Pelements"])
                
                
                print(sentence0[0]+" might be "+" ".join(array))
                
            if sentence0[5] == "D" or sentence0[5] =="d":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"Delements"]) != True:
                    
                        array.append(df.loc[cnt,"Delements"])
                
                
                print(sentence0[0]+" might be "+" ".join(array))

        if indx == 18:
    
            array=[]
            
            if sentence0[5] == "used" and sentence0[8] =="manufacture":
                
                for cnt in range (fulllength):
                    
                    if sentence0[10]==df.loc[cnt,"used"]:
                        
                        array.append(df.loc[cnt,"used"])
                        
                print(" ".join(array))
                
                if len(array) == 1:
                    
                    for cnt in range (fulllength):
                        if array[0]==df.loc[cnt,"used"]:
                            print(sentence0[3]+" is "+ df.loc[cnt,"Selements"])

        if indx == 19:
    
            array=[]
                
            if sentence0[6] == "used" and sentence0[8] =="identify": 
                
                for cnt in range (fulllength):
                    
                    if sentence0[10]==df.loc[cnt,"state"]:
                        
                        array.append(df.loc[cnt,"identify"])
                        
                print(" ".join(array))
                    
                if len(array) == 1:
                    
                    for cnt in range (fulllength):
                        if array[0]==df.loc[cnt,"identify"]:
                            
                            print(sentence0[11]+" is "+ df.loc[cnt,"identify"])
                            print(sentence0[3]+" is "+ df.loc[cnt,"Selements"])

        if indx == 20:
            if sentence0[7] == "solid":
                
                for cnt in range (len(df.index)):
                    
                    if sentence0[8]==df.loc[cnt,"solid"]:
                        
                        print(sentence0[0]+" or "+sentence0[3]+" should be "+df.loc[cnt,"first"]+" and "+df.loc[cnt,"second"])
            
            if sentence0[7] == "solution":
                
                for cnt in range (len(df.index)):
                    
                    if sentence0[8]==df.loc[cnt,"solution"]:
                        
                        print(sentence0[0]+" or "+sentence0[3]+" should be "+df.loc[cnt,"first"]+" and "+df.loc[cnt,"second"])
                    
            if sentence0[7] == "gas":
                
                for cnt in range (len(df.index)):
                    
                    if sentence0[8]==df.loc[cnt,"gas"]:
                        
                        print(sentence0[0]+" or "+sentence0[3]+" should be "+df.loc[cnt,"first"]+" and "+df.loc[cnt,"second"])
                    
        if indx == 26:
            for cnt in range (len(df.index)):
                
                                
                if sentence0[8]==df.loc[cnt,"heated"]:
                        
                    print(sentence0[4]+" is "+df.loc[cnt,"first"] ) 

        if indx == 27:
            for cnt in range (len(df.index)):
                    
                    if sentence0[12]==df.loc[cnt,"flame"]:
                        
                        print(sentence0[8]+" is "+df.loc[cnt,"first"] )

        if indx == 29:
        
            if sentence0[6] == "S" or sentence0[6] =="s":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"Selements"]) != True:
                        
                        array.append(df.loc[cnt,"Selements"])
                
                
                print(sentence0[2].replace(",","")+" might be "+" ".join(array))
                
            if sentence0[6] == "P" or sentence0[6] =="p":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"Pelements"]) != True:
                        
                        array.append(df.loc[cnt,"Pelements"])
                
                
                print(sentence0[2]+" might be "+" ".join(array))
                
            if sentence0[6] == "D" or sentence0[6] =="d":
                array=[]
                for cnt in range (fulllength):
                    
                    if pd.isnull(df.loc[cnt,"Delements"]) != True:
                        
                        array.append(df.loc[cnt,"Delements"])
                
                
                print(sentence0[2]+" might be "+" ".join(array))
                  
    