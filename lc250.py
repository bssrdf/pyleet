
import os

_, _, filenames = next(os.walk('./'))
flist = [f.split('.')[0] for f in filenames if f.endswith('.py')]   
flist = set((f.lower() for f in flist))
finished = 0
newfields = []
with open('LC250.txt','r') as infile:
    for line in infile.readlines():
        fields = line.split()        
        prob_name = ''.join(fields[1:-1])
        prob_name = prob_name.replace('(','')
        prob_name = prob_name.replace(')','')
        if prob_name.lower() in flist:
            finished += 1
            mark = ':heavy_check_mark:'
        else:
            mark = ':heavy_multiplication_x:'
        #newfields ='- '+mark+'  '+fields[0]+'  '+prob_name+'\n' 
        newfields.append('- '+mark+'  '+fields[0]+'  '+prob_name+'\n') 
        #outfile.write(newfields)
summary = "\n## **%d** have been finished with **%d** left" %(finished, 250-finished)
with open('LC250.md','w') as outfile:
    outfile.write("# Leetcode 前 400 重点 250 题")    
    outfile.write("\n\n")    
    outfile.write("---")    
    outfile.write("\n\n")    
    outfile.write(summary)
    outfile.write("\n---")
    for line in newfields:
        outfile.write(line)




#with open('LC250.md','a') as outfile:
#    outfile.write("\n---")
#    outfile.write(summary)
print(summary)
