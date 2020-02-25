import numpy as np

a = np.arange(10, 30).reshape(4, 5)

red    = a[0, 1:4] 
blue   = a[0:4:2, 4] 
green  = a[:3, 2] 
lightblue = a[:, 1::2]  #not done yet
yellow = a[:1, 0]
print('red:',red,'\nblue:',blue,'\ngreen:\n',green,'\nlightblue:',lightblue,'\nyellow:', yellow)

