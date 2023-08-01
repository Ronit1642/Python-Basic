import pickle
a=open('E:\AAAAA.docx','ab')
b=pickle.dump(a,a)
a.close()
g=open('E:\AAAAA.docx','rb')
e=pickle.load(g)
g.close()
print(e)
