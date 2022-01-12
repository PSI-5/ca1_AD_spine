import os
import numpy as np 

D1=np.arange(0.61,0.71,0.01)

to=np.arange(0,0.11,0.01)

params=[]

for i in D1:
    for j in to:
        params.append(str(i)+' '+str(j))

for k in range(len(params)):
 os.system('python3 ~/Desktop/ip3_ad_codes/ctrl_49_ip3r_ip3c_5/stutzmann.py ' + params[k])




