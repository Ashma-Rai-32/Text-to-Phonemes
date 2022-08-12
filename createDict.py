import pandas as pd
# xl= pd.ExcelFile('dictionaryPhonemes.xlsx')
# print(xl.sheet_names)
# file=pd.read_excel(xl,sheet_name='Sheet1')
# file.to_csv('dictionaryPhonemes.txt', header=False)

# #replace unnecessary symbols
# with open('dictionaryPhonemes.txt','r') as file:
#     data=file.read()
#     data=data.replace(",",' ')
#     # # data=data.replace("\\",'|')
#     # data=data.replace("  "," _")

# with open('dictionaryPhonemes.txt','w') as file:
#     file.write(data)

dict={}
file=open("dictionaryPhonemes.txt")
for line in file:
    key,value=line.split()
    dict[key]=value
print(dict)