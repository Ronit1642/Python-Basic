import pickle 
a=open("jnv.dat","rb")
b=pickle.load(a)
print(b)
a.close()
