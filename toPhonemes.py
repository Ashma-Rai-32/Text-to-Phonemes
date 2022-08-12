from asyncore import loop
from contextlib import nullcontext
from operator import contains
from xml.etree.ElementInclude import include
import pandas as pd
import extractWordsAsList as ewal
from createDict import dict

#replace hexcodes in 'extractedWords' list with phonemes referring to 'dict' list
#save it in new file toPhonemes.txt

newfile=open('toPhonemes.txt',mode='a')

count=len(ewal.extractedWords)
print(count)

for i in range(0,count):
    temp=len(ewal.extractedWords[i])
    for j in range(0,temp):
        tempx=len(ewal.extractedWords[i][j])
        for k in range(0,tempx,12):
            new=ewal.extractedWords[i][j][k:k+12]
            value=dict[new]
            newfile.write(value)
        newfile.write('\n')
    newfile.write('\n')

newfile.close()

#phonemes of inputTextToConvertHere.txt is extracted in toPhonemes.txt file




# contents=file.readlines()
# for line in contents:
#     reading=line.split()
#     count=len(reading)
#     print(count)
#     for i in range(0,count):
#         for j in range(0,reading[i]):
            
#             extractedPhoneme={}
#             extractedPhoneme+=reading[i][j]
#         print(reading)


# for line in file:
#     for character in line:
#         if (character=='\n'): 
#             break
#         elif(character==' '):
#             key=file.read(1)
#             newfile.write(key)
#             break
#         else:
#             key=file.read(12)
#             value=dict[key]
#             print(key,value)
#             newfile.write(value)

