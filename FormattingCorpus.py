f=open("corpus.txt","r")
f2=open("formatted.txt","a")
lines=f.readlines()

for line in lines:
    l=line.strip().split('\t')
    if(l[0]!='#' and l[0]!=' ' and len(l)>4):
        f2.write(l[1]+'\t'+l[4]+'\n')
       
f.close()
f2.close()
