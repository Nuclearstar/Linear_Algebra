import numpy as np

a = np.matrix('2 2;-2 -2')

y1,y2 = np.linalg.eigvals(a);

print('Matrix A : ')
print(a);
print('\n')
if(y1 == y2 ) or isinstance(y1, complex) or isinstance(y2, complex):
	print('The matrix A is not diagonalisable')
	print('\n')
	print('\n')
else:
	print('The matrix A is diagonalisable')
	print('\n')
	print('The eigen values of A are : ')
	print(y1);
	print(y2);
	print('\n')

print('------------------------------------------------------------------------------------')
print('\n')
print('Matrix A : ')
a = np.matrix('2 0 ; 2 -2')

y1,y2 = np.linalg.eigvals(a);

print(a);
print('\n')
if(y1 == y2) or isinstance(y1, complex) or isinstance(y2, complex):
	print('The matrix A is not diagonalisable')
	print('\n')
	print('\n')
else:
	print('The matrix A is diagonalisable')
	print('\n')
	print('The eigen values of A are : ')
	print(y1);
	print(y2);
	print('\n')

print('------------------------------------------------------------------------------------')
print('\n')
print('Matrix A : ')
a = np.matrix('2 0; 2 2')

y1,y2 = np.linalg.eigvals(a);

print(a);
print('\n')
if(y1 == y2) or isinstance(y1, complex) or isinstance(y2, complex):
	print('The matrix A is not diagonalisable')
	print('\n')
	print('\n')
else:
	print('The matrix A is diagonalisable')
	print('\n')
	print('The eigen values of A are : ')
	print(y1);
	print(y2);
	print('\n')
print('------------------------------------------------------------------------------------')
