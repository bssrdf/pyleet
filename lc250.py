
import os

_, _, filenames = next(os.walk('./'))
flist = [f.split('.')[0] for f in filenames if f.endswith('.py')]   
flist = set((f.lower() for f in flist))
finished = 0
with open('LC250.txt','r') as infile, open('LC250.md','w') as outfile:
    for line in infile.readlines():
        fields = line.split()        
        prob_name = ''.join(fields[1:-1])
        if prob_name.lower() in flist:
            finished += 1
            mark = ':heavy_check_mark:'
        else:
            mark = ':heavy_multiplication_x:'
        newfields ='- '+mark+'  '+fields[0]+'  '+prob_name+'\n' 
        outfile.write(newfields)
summary = "\n##**%d** have been finished with **%d** left" %(finished, 250-finished)
with open('LC250.md','a') as outfile:
    outfile.write("\n---")
    outfile.write(summary)
print(summary)
