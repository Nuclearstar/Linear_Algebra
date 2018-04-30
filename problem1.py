import numpy as np 

a1 = np.matrix([[1],[1],[0]]);
a2 = np.matrix('1;1;-1');

a = np.matrix('1 1;0 1;1 -1');

temp = np.dot(np.transpose(a) , a)

print("The projection matrix P is given by, \n\n P = A * (A * A^T) A^T")
print('\n')
print('\n')

print(' A * A^T  = ');
print(temp)
print('\n')
print('\n')

det = temp[0,0] * temp [1,1] - temp[0,1] * temp[1,0];

temp[0,0],temp[1,1] = temp[1,1],temp[0,0];
temp[0,1] = -1 * temp[0,1];
temp[1,0] = -1 * temp[1,0];

temp = (1/det) * temp

print(" ( A * A^T ) inverse = ")
print(temp)
print('\n')
print('\n')

temp = np.dot(a,temp)

print(" A * (A * A^T) = ")
print(temp)
print('\n')
print('\n')

temp = np.dot(temp,np.transpose(a))


print(" P = ")
print(temp)
print('\n')
print('\n')