


with open('LC250.txt','r') as infile, open('LC250.md','w') as outfile:
    for line in infile.readlines():
        fields = line.split()
        #newfields ='- []'+'  '+fields[0]+'  '+''.join(fields[1:-1])+'\n' 
        newfields ='- :heavy_check_mark: '+'  '+fields[0]+'  '+''.join(fields[1:-1])+'\n' 
        #print(len(fields)) :heavy_multiplication_x:
        outfile.write(newfields)
