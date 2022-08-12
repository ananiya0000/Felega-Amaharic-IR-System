# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 18:17:53 2022

@author: anani
"""
import json
from stemmer import stemmer
from lexicalAnalyzer import lex_analyzer
from termweighting import termWeighting
from stopwordRemover import removestopwords

def indexer():
    data={}
    i=0
    filepath=[]
    k=1
    while k<=50:
        strr="./pages/Document"+str(k)+".txt"
        filepath.append(strr)
        k+=1
    while(i<len(filepath)):
        doc=open(filepath[i],"r",encoding="utf-8")  
        #call lexical analyzer and stopword remover function before split
        docanalyzed=lex_analyzer(doc.read())
        docanalyzed=removestopwords(docanalyzed)
        document=docanalyzed.split()
        data["doc"+str(i)]={}
        for word in document:
            #you can call stemmer on each word here
            word=stemmer(word)
            if(word==""):
                continue
            if(data["doc"+str(i)].get("length")):
                data["doc"+str(i)]["length"]=data["doc"+str(i)]["length"]+1
            else:
                data["doc"+str(i)]["length"]=1 
            
            if(data["doc"+str(i)].get(word)):
                data["doc"+str(i)][word]=data["doc"+str(i)][word]+1
            else:
                data["doc"+str(i)][word]=1
        print(filepath[i])
        doc.close()
        i+=1
    indexfile=open("./indexed.json","w",encoding="utf-8")
    json_object=json.dumps(data,indent=4,)
    indexfile.write(json_object)
    #call termweighter Here
    termWeighting(data)

indexer()
