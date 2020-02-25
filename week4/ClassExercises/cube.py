import numpy as np

#[z,y,x]
a = np.arange(0, 27).reshape((3, 3, 3))

# Slice out [12 13 14] from the above cube using only one slice. e.g: a[:,:,:]
print('Slice out 12,13,14]\n',a[1:,1:,0:])
# Slice out [3 12 21].
print('Slice out [3,12,21]\n', a[:,:,:])
# Slice out all y-values where x is 2 and z is 0.
print('All y values where x is 2 and z is 0\n', a[0:,:,2])