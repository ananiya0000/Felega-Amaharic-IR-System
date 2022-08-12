# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 18:17:53 2022

@author: anani
"""
import math
import json

def termWeighting(datafromIndexer):
    data=datafromIndexer
    Idf={}
    Tf={}
    TfIdf={}
    docCount=0
    for doc in data:
        Tf[doc]={}
        for word in data[doc]:
            tf=data[doc][word]/data[doc]["length"]
            Tf[doc][word]=tf
            if(Idf.get('{}'.format(word))==None):
                Idf[word]=1
            else:
                Idf[word]=Idf[word]+1

        docCount+=1
    Idf.pop("length")
    for word in Idf:
        Idf[word]=math.log2(docCount/Idf[word])
    
    for doc in Tf:
        TfIdf[doc]={}
        for word in Idf:
            if(Tf[doc].get(word)):
                TfIdf[doc][word]=Tf[doc][word]*Idf[word]
    termWeights=open("./termWeights.json","w",encoding="utf-8")
    json_object=json.dumps(TfIdf,indent=4,)
    termWeights.write(json_object)
    return TfIdf    
