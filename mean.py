import numpy as np
x=[0,1,2,3,4,5,6,7,8]
x=np.array(x)
x=np.array(x).reshape(3,3)
y ={}
su =[x[: ,0:].sum(axis=0).tolist(),x[0: ,].sum(axis=1).tolist(),x.sum()]
minimum=[x[: ,0:].min(axis=0).tolist(),x[0: ,].min(axis=1).tolist(),x.min()]
maximum =[x[: ,0:].max(axis=0).tolist(),x[0: ,].max(axis=1).tolist(),x.max()]
stand =[x[: ,0:].std(axis=0).tolist(),x[0: ,].std(axis=1).tolist(),x.std()]
r=[x[: ,0:].var(axis=0).tolist(), x[0: ,].var(axis=1).tolist(), x.var()]
z=[x[: ,0:].mean(axis=0).tolist(),x[0: ,].mean(axis=1).tolist(),x.mean()]
y["mean"]=z
y["variance"]=r
y["standered deviation"]=stand
y["max"]=maximum
y["min"]=minimum
y["sum"]=su

print(y)
