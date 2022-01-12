import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import defaultdict
import matplotlib.cm as cm


columns=defaultdict(list)
columns_56=defaultdict(list)
columns_exp=defaultdict(list)
D1=np.arange(0.61,0.71,0.01)
#D1=D1[1::5]
colors = cm.rainbow(np.linspace(0, 1, len(D1)))
j=0
plt.figure()
for i in D1:
    columns=defaultdict(list)
    with open('stutzmann_'+str(i)+'.csv') as f:

      reader = csv.DictReader(f,delimiter='\t') # read rows into a dictionary format
      for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(float(v)) 
    
    plt.plot(np.array(columns['to'])[1:],(np.array(columns['Ca_F_CaF0_ad'])[1:]/np.array(columns['Ca_F_CaF0'])[1:]),label=str(round(i,3)),color=colors[j])

    j=j+1

with open('foskett_data.csv') as f:

  reader = csv.DictReader(f,delimiter=',') # read rows into a dictionary format
  for row in reader: # read a row as {column1: value1, column2: value2,...}
    for (k,v) in row.items(): # go over each column name and value
        columns_exp[k].append(float(v))       

plt.plot(np.array([10,25,50,100])/1000,columns_exp['RATIO'][:-1],color='k')
plt.legend()
plt.xlabel('time of UV exposure (s)')
plt.ylabel('ratio(df)')



plt.show()
