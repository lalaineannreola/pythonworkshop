count = 0.00

line=open("dna.txt").read()
for x in range (0,len(line)):
    if(line[x]=='G' or line [x] == 'C'):
        count=count+1

print "The file contains", count, "C and G."
prc=(count/len(line))*100
print "The percentage of GC of DNA is: "+str(prc)+"%"
