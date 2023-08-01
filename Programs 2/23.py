import pickle
a=open('dogs.bin','rb')
nd=pickle.load(a)
print(nd)
a.close()
