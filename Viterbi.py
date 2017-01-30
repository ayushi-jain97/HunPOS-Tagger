from collections import OrderedDict as od

f=open("train.txt","r")

lines=f.readlines()
prior={}
transition=[]
count_label={}
ref=od()
index=[]



x=0
for line in lines:
	l=line.strip().split('\t')
	if len(l)>1:
		try:
			count_label[l[1]]=count_label[l[1]]+1
		except:
			ref[l[1]]=x
			index.append(l[1])
			x=x+1
			count_label[l[1]]=1

total_label=len(count_label)
n=0.0
for i in count_label.keys():
	n=n+count_label[i]

print "Total states ", total_label
#print (label)
#print s
#print ref
#print index

for i in count_label.keys():
	prior[i]=(count_label[i]/n)


for i in range(total_label):
	transition.append([])
	for j in range(total_label):
		transition[i].append(0)

#print transition

for i in range(len(lines)-1):
	l1=lines[i].strip().split('\t')
	l2=lines[i+1].strip().split('\t')
	#print l1,l2
	if len(l1)==2 and len(l2)==2:	
		a=l1[1];b=l2[1]
		transition[ref[a]][ref[b]]=transition[ref[a]][ref[b]]+1


for i in range(len(transition)):
	s=float(sum(transition[i]))
	for j in range(len(transition[i])):
		transition[i][j]=transition[i][j]/s


emission=[]

for i in range(total_label):
	emission.append({})

for line in lines:
	l=line.strip().split('\t')
	l[0]=l[0].lower()
	if len(l)==2:
		try:
			emission[ref[l[1]]][l[0]]=emission[ref[l[1]]][l[0]]+1
		except:
			emission[ref[l[1]]][l[0]]=1





for i in range(len(emission)):
	s=0.0
	for j in emission[i].keys():
		s=s+emission[i][j]
	for j in emission[i].keys():
		emission[i][j]=emission[i][j]/s




def viterbi(sent):
	t=[]
	path=[]
	sent=sent.strip().split()
	for i in range(len(sent)):
		sent[i]=sent[i].lower()
	for i in range(total_label):
		t.append([])
		path.append([])
		for j in range(len(sent)):
			t[i].append(0.0)
			path[i].append(0)
	
	for i in range(total_label):	
		try:
			t[i][0]=prior[index[i]]*emission[i][sent[0]]
			#print prior[index[i]],emission[i][sent[0]]
			#print prior[index[i]]*emission[i][sent[0]]
			#print index[i]
		except:
			pass
	
	for i in range(1,len(sent)):
		for j in range(total_label):
			for k in range(total_label):
				
				if t[k][i-1]*transition[k][j] > t[j][i]:
					t[j][i]=t[k][i-1]*transition[k][j]
					path[j][i]=k
			try:
				t[j][i]=t[j][i]*emission[j][sent[i]]
			except:
				t[j][i]=0
	
	m=0.0
	arg=0		
	for i in range(total_label):
		if t[i][len(sent)-1]>m:
			m=t[i][len(sent)-1]
			arg=i
	#print m
	ans=[]
	for i in range(len(sent)-1,-1,-1):
		ans.append(index[arg])
		arg=path[arg][i]
	ans.reverse()
	ans=' '.join(ans)
	#print path
	return ans
		


print viterbi("announce new base rates to defend the down side restated")

s=''
final_tag=''
comp=0
for i in range(len(lines)):
	l=lines[i].strip().split('\t')
	s=s+l[0]+' '
	if l[0]=='.':
		final_tag=final_tag+viterbi(s)+' '
		s=s.split()
		comp=comp+len(s)
		s=''

print final_tag

error=0


tag_pred=final_tag.split()
tag_true=[]

for line in lines:
	l=line.strip().split('\t')
	tag_true.append(l[1])

for i in range(len(tag_pred)):
	if tag_pred[i]!=tag_true[i]:
		error=error+1

total=len(tag_pred)
print "The total number of words that were not predicted correctly are",error
print "Accuracy:",((total-error)*100.0)/total

import sklearn.metrics as metrics
from pandas_ml import ConfusionMatrix

print metrics.accuracy_score(tag_true,tag_pred)

print metrics.precision_score(tag_true,tag_pred,average='micro')

cm=ConfusionMatrix(tag_true,tag_pred)
cm.print_stats()

