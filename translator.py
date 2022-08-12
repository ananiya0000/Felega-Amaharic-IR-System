# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 18:17:53 2022

@author: anani
"""
import re

from matplotlib.pyplot import flag

am_to_en={
  'ሀ': "he",
  'ሁ': "hu",
  'ሂ': "hi",
  'ሃ': "he",
  'ሄ': "hE",
  'ህ': "h",
  'ሆ': "ho",
  'ለ': "le",
  'ሉ': "lu",
  'ሊ': "li",
  'ላ': "la",
  'ሌ': "lE",
  'ል': "l",
  'ሎ': "lo",
  'ሏ': "lWa",
  'ሐ': "he",
  'ሑ': "hu",
  'ሒ': "hi",
  'ሓ': "he",
  'ሔ': "hE",
  'ሕ': "h",
  'ሖ': "ho",
  'ሗ': "hWa",
  'መ': "me",
  'ሙ': "mu",
  'ሚ': "mi",
  'ማ': "ma",
  'ሜ': "mE",
  'ም': "m",
  'ሞ': "mo",
  'ሟ': "mWa",
  'ሠ': "se",
  'ሡ': "su",
  'ሢ': "si",
  'ሣ': "sa",
  'ሤ': "sE",
  'ሥ': "s",
  'ሦ': "so",
  'ሧ': "sWa",
  'ረ': "re",
  'ሩ': "ru",
  'ሪ': "ri",
  'ራ': "ra",
  'ሬ': "rE",
  'ር': "r",
  'ሮ': "ro",
  'ሯ': "rWa",
  'ሰ': "se",
  'ሱ': "su",
  'ሲ': "si",
  'ሳ': "sa",
  'ሴ': "sE",
  'ስ': "s",
  'ሶ': "so",
  'ሷ': "sWa",
  'ሸ': "xe",
  'ሹ': "xu",
  'ሺ': "xi",
  'ሻ': "xa",
  'ሼ': "xE",
  'ሽ': "x",
  'ሾ': "xo",
  'ሿ': "xWa",
  'ቀ': "qe",
  'ቁ': "qu",
  'ቂ': "qi",
  'ቃ': "qa",
  'ቄ': "qE",
  'ቅ': "q",
  'ቆ': "qo",
  'ቈ': "qWe",
  'ቊ': "qu",
  'ቋ': "qWa",
  'ቌ': "qWE",
  'ቍ': "qW",
  'በ': "be",
  'ቡ': "bu",
  'ቢ': "bi",
  'ባ': "ba",
  'ቤ': "bE",
  'ብ': "b",
  'ቦ': "bo",
  'ቧ': "bWa",
  'ቨ': "ve",
  'ቩ': "vu",
  'ቪ': "vi",
  'ቫ': "va",
  'ቬ': "vE",
  'ቭ': "v",
  'ቮ': "vo",
  'ቯ': "vWa",
  'ተ': "te",
  'ቱ': "tu",
  'ቲ': "ti",
  'ታ': "ta",
  'ቴ': "tE",
  'ት': "t",
  'ቶ': "to",
  'ቷ': "tWa",
  'ቸ': "ce",
  'ቹ': "cu",
  'ቺ': "ci",
  'ቻ': "ca",
  'ቼ': "cE",
  'ች': "c",
  'ቾ': "co",
  'ቿ': "cWa",
  'ኀ': "he",
  'ኁ': "hu",
  'ኂ': "hi",
  'ኃ': "he",
  'ኄ': "hE",
  'ኅ': "h",
  'ኆ': "ho",
  'ኈ': "hWe",
  'ኊ': "hWi",
  'ኋ': "hWa",
  'ኌ': "hWE",
  'ኍ': "hW",
  'ነ': "ne",
  'ኑ': "nu",
  'ኒ': "ni",
  'ና': "na",
  'ኔ': "nE",
  'ን': "n",
  'ኖ': "no",
  'ኗ': "nWa",
  'ኘ': "Ne",
  'ኙ': "Nu",
  'ኚ': "Ni",
  'ኛ': "Na",
  'ኜ': "NE",
  'ኝ': "N",
  'ኞ': "No",
  'ኟ': "NWa",
  'አ': "a",
  'ኡ': "u",
  'ኢ': "i",
  'ኣ': "a",
  'ኤ': "E",
  'እ': "I",
  'ኦ': "o",
  'ኧ': "e",
  'ከ': "ke",
  'ኩ': "ku",
  'ኪ': "ki",
  'ካ': "ka",
  'ኬ': "kE",
  'ክ': "k",
  'ኮ': "ko",
  'ኰ': "ko",
  'ኲ': "kWi",
  'ኳ': "kWa",
  'ኴ': "kWE",
  'ኵ': "kW",
  'ኸ': "Ke",
  'ኹ': "hu",
  'ኺ': "hi",
  'ኻ': "he",
  'ኼ': "hE",
  'ኽ': "h",
  'ኾ': "ho",
  'ዀ': "KWe",
  'ዂ': "KWi",
  'ዃ': "KWa",
  'ዄ': "KWE",
  'ዅ': "KW",
  'ወ': "we",
  'ዉ': "wu",
  'ዊ': "wi",
  'ዋ': "wa",
  'ዌ': "wE",
  'ው': "w",
  'ዎ': "wo",
  'ዐ': "e",
  'ዑ': "u",
  'ዒ': "i",
  'ዓ': "e",
  'ዔ': "E",
  'ዕ': "e",
  'ዖ': "o",
  'ዘ': "ze",
  'ዙ': "zu",
  'ዚ': "zi",
  'ዛ': "za",
  'ዜ': "zE",
  'ዝ': "z",
  'ዞ': "zo",
  'ዟ': "zWa",
  'ዠ': "Ze",
  'ዡ': "Zu",
  'ዢ': "Zi",
  'ዣ': "Za",
  'ዤ': "ZE",
  'ዥ': "Z",
  'ዦ': "Zo",
  'ዧ': "ZWa",
  'የ': "ye",
  'ዩ': "yu",
  'ዪ': "yi",
  'ያ': "ya",
  'ዬ': "yE",
  'ይ': "y",
  'ዮ': "yo",
  'ደ': "de",
  'ዱ': "du",
  'ዲ': "di",
  'ዳ': "da",
  'ዴ': "dE",
  'ድ': "d",
  'ዶ': "do",
  'ዷ': "dWa",
  'ጀ': "je",
  'ጁ': "ju",
  'ጂ': "ji",
  'ጃ': "ja",
  'ጄ': "jE",
  'ጅ': "j",
  'ጆ': "jo",
  'ጇ': "jWa",
  'ገ': "ge",
  'ጉ': "gu",
  'ጊ': "gi",
  'ጋ': "ga",
  'ጌ': "gE",
  'ግ': "g",
  'ጎ': "go",
  'ጐ': "go",
  'ጒ': "gWi",
  'ጓ': "gWa",
  'ጔ': "gWE",
  'ጕ': "gW",
  'ጠ': "Te",
  'ጡ': "Tu",
  'ጢ': "Ti",
  'ጣ': "Ta",
  'ጤ': "TE",
  'ጥ': "T",
  'ጦ': "To",
  'ጧ': "TWa",
  'ጨ': "Ce",
  'ጩ': "Cu",
  'ጪ': "Ci",
  'ጫ': "Ca",
  'ጬ': "CE",
  'ጭ': "C",
  'ጮ': "Co",
  'ጯ': "CWa",
  'ጰ': "Pe",
  'ጱ': "Pu",
  'ጲ': "Pi",
  'ጳ': "Pa",
  'ጴ': "PE",
  'ጵ': "P",
  'ጶ': "Po",
  'ጷ': "PWa",
  'ጸ': "SSe",
  'ጹ': "SSu",
  'ጺ': "SSi",
  'ጻ': "SSa",
  'ጼ': "SSE",
  'ጽ': "SS",
  'ጾ': "SSo",
  'ጿ': "SSWa",
  'ፀ': "SSe",
  'ፁ': "SSu",
  'ፂ': "SSi",
  'ፃ': "SSa",
  'ፄ': "SSE",
  'ፅ': "SS",
  'ፆ': "SSo",
  'ፈ': "fe",
  'ፉ': "fu",
  'ፊ': "fi",
  'ፋ': "fa",
  'ፌ': "fE",
  'ፍ': "f",
  'ፎ': "fo",
  'ፏ': "fWa",
  'ፐ': "pe",
  'ፑ': "pu",
  'ፒ': "pi",
  'ፓ': "pa",
  'ፔ': "pE",
  'ፕ': "p",
  'ፖ': "po",
  'ፗ': "pWa",
}

def am_to_translator(word,lang):
    translated=""
    if(lang=='am'):
        tokens=word
        for token in tokens:
            if(am_to_en.get('{}'.format(token))):
                translated+=am_to_en['{}'.format(token)]
    elif(lang=='en'):
        i=0
        while(i<len(word)-1):
            if(re.search('[aeiou]',word[i+1],flags=re.IGNORECASE)):
                token=word[i]+word[i+1]
                value={j for j in am_to_en if am_to_en[j]==token}
                val=str(value)
                if(val[2]!=None):
                    translated+=val[2]
                i+=2
            else:
                value={j for j in am_to_en if am_to_en[j]==word[i]}
                val=str(value)
                if(val[2]!=None and val[2]!="ኧ"):
                    translated+=val[2]
                i+=1
            if(i+1==len(word) and re.search('[^aeiou]',word[i],flags=re.IGNORECASE)):
                value={j for j in am_to_en if am_to_en[j]==word[i]}
                val=str(value)
                if(val[2]!=None and val[2]!="ኧ"):
                    translated+=val[2]

    return translated



#translated=am_to_translator('ቅጠላቅጠል','am')
#translated2=am_to_translator('qTelaqTel','en')



































    # elif(lang=='enn'):
    #     tokens=re.findall('.{1,2}',word)
    #     print(tokens)
    #     for token in tokens:
    #         #print(token)
    #         charlen2letters=re.findall("[^aeiou][aeiou]",token,flags=re.IGNORECASE)
    #         #print(charlen2letters)
    #         if(charlen2letters!=[]):
    #             value={i for i in am_to_en if am_to_en[i]==token}
    #             val=str(value)
    #             if(val[2]!=None):
    #                 translated+=val[2]
    #         else:
    #             for tok in token:
    #                #print(tok)
    #                value={i for i in am_to_en if am_to_en[i]==tok} 
    #                val=str(value)
    #                if(val[2]!=None and val[2]!="ኧ"):
    #                 translated+=val[2]