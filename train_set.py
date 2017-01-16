f=open("test.txt","r")
f2=open("test_set.txt","a")
f3=open("test_label.txt","a")
lines=f.readlines()
for line in lines:
    l=line.strip().split('\t')
    f2.write(l[0]+'\n')
    f3.write(l[1]+'\n')
f.close()
f2.close()
f3.close()
    
