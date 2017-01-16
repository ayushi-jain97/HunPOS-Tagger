f1=open("formatted.txt","r")
f2=open("train.txt","a")
f3=open("test.txt","a")
lines=f1.readlines()
n=len(lines)
a=(int)(0.8*n)
for i in range(a):
    f2.write(lines[i])
for i in range(a,n,1):
    f3.write(lines[i])
f1.close()
f3.close()
f2.close()
