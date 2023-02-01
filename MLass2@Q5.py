n=input()
d={'uppercase':0,'lowercase':0}
for i in n:
    if i.isupper():
        d["uppercase"]+=1
    elif i.islower():
        d['lowercase']+=1
    else:
        pass
print('No. of Upper-case characters:',d['uppercase'])
print('No. of lower-case characters:',d['lowercase'])
