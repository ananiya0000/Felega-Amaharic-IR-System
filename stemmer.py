# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 18:17:53 2022

@author: anani
"""

from translator import am_to_translator
import re

suffix_list ="ኦችኣችኧውንንኣ|ኦችኣችህኡ|ኦችኣችኧውን|ኣችኧውንንኣ|ኦችኣችኧው|ኢዕኧልኧሽ|ኦችኣችን|ኣውኢው|ኣችኧውኣል|ችኣት|ችኣችህኡ|ችኣችኧው|ኣልኧህኡ|ኣውኦች|ኣልኧህ|ኣልኧሽ|ኣልችህኡ|ኣልኣልኧች|ብኣችኧውስ|ብኣችኧው|ኣችኧውን|ኣልኧች|ኣልኧን|ኣልኣችህኡ|ኣችህኡን|ኣችህኡ|ኣችህኡት|ውኦችንንኣ|ውኦችን|ኣችኧው|ውኦችኡን|ውኦችኡ|ውንኣ|ኦችኡን|ኦውኦች|ኝኣንኧትም|ኝኣንኣ|ኝኣንኧት|ኝኣን|ኝኣውም|ኝኣው|ኣውኣ|ብኧትን|ኣችህኡም|ችኣችን|ኦችህ|ኦችሽ|ኦችኡ|ኦችኤ|ኦውኣ|ኦቿ|ችው|ችኡ|ኤችኡ|ንኧው|ንኧት|ኣልኡ|ኣችን|ክኡም|ክኡት|ክኧው|ችን|ችም|ችህ|ችሽ|ችን|ችው|ይኡሽን|ይኡሽ|ውኢ|ኦችንንኣ|ኣውኢ|ብኧት|ኦች|ኦችኡ|ውኦን|ኝኣ|ኝኣውን|ኝኣው|ኦችን|ኣል|ም|ሽው|ክም|ኧው|ትም|ውኦ|ውም|ውን|ንም|ሽን|ኣች|ኡት|ኢት|ክኡ|ኤ|ህ|ሽ|ኡ|ሽ|ክ|ች|ኡን|ን|ም|ንኣ|ው";
prefix_list ="ስልኧምኣይ|ይኧምኣት|ዕንድኧ|ይኧትኧ|ብኧምኣ|ብኧትኧ|ዕኧል|ስልኧ|ምኧስ|ዕይኧ|ይኣል|ስኣት|ስኣን|እንደ|ስኣይ|ስኣል|ይኣስ|ይኧ|ልኧ|ክኧ|እን|አል|አስ|ትኧ|አት|አን|አይ|ይ|አ|እ|በ"

suffix_arr=[]
prefix_arr=[]

def stemmer(word):
    
    word=am_to_translator(word,"am")
    stemmedword=""
    suffix_list_split=suffix_list.split("|")
    for suffix in suffix_list_split:
        suffix_arr.append(am_to_translator(suffix,"am"))
    
    prefix_list_split=prefix_list.split("|")
    for prefix in prefix_list_split:
        prefix_arr.append(am_to_translator(prefix,"am"))

    
    for suffix_eng in suffix_arr:
        if(word.endswith(suffix_eng)):
            word=word.rstrip(suffix_eng)

    for prefix_eng in prefix_arr:
        if(word.startswith(prefix_eng)):
            word=word.removeprefix(prefix_eng)
    #ቅጠላቅጠል type
    infix=re.findall('(.[^aeiou])[aeiou]',word,flags=re.IGNORECASE)
    if(len(infix)>1):
        if(infix[0]==infix[1]):
            tempword=""
            i=0
            for w in word:
                if(i!=0 and w==infix[0][0]):
                    word=tempword
                    break
                if(w==infix[0][0]):
                    i+=1
                tempword+=w
    stemmedword=am_to_translator(word,"en")
    return stemmedword

#stemmedwordfinal=stemmer("በክልሎ")


