from pandas_ml import ConfusionMatrix
import sklearn.metrics as metrics

f1=open("test_label.txt","r")
f2=open("output.txt","r")
l1=f1.readlines()
l2=f2.readlines()
label_true=[]
label_predicted=[]
for i in range(len(l1)):
    s1=l1[i].strip().split('\t')
    s2=l2[i].strip().split('\t')
    if(len(s1)>0 and len(s2)>1):
        label_true.append(s1[0])
        label_predicted.append(s2[1])



##print len(label_original),len(label_predicted)

print metrics.accuracy_score(label_true,label_predicted)
print metrics.recall_score(label_true,label_predicted,average='micro')
print metrics.precision_score(label_true,label_predicted,average='micro')
print metrics.f1_score(label_true,label_predicted,average='micro')
cm=ConfusionMatrix(label_true,label_predicted)
cm.print_stats()
