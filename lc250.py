
import os

_, _, filenames = next(os.walk('./'))
flist = [f.split('.')[0] for f in filenames if f.endswith('.py')]   
print(flist[:10])
flist = set((f.lower() for f in flist))
with open('LC250.txt','r') as infile, open('LC250.md','w') as outfile:
    for line in infile.readlines():
        fields = line.split()
        #newfields ='- []'+'  '+fields[0]+'  '+''.join(fields[1:-1])+'\n' 
        prob_name = ''.join(fields[1:-1])
        if prob_name.lower in flist:
            newfields ='- :heavy_check_mark: '+'  '+fields[0]+'  '+prob_name+'\n' 
        else:
            newfields ='- :heavy_multiplication_x: '+'  '+fields[0]+'  '+prob_name+'\n' 
        #print(len(fields)) 
        outfile.write(newfields)

