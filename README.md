# Linear_Algebra

1. Design a program to ﬁnd the projection matrix P onto the space spanned by 2 vectors.
2. Design a program to check which of the matrices cannot be diagonalised.

ALGORITHM

To ﬁnd the projection matrix P onto the space spanned by 2 vectors
1. Give 2 input vectors whose projection matrix has to be found.
2. Find the transpose of those matrices.
3. Then ﬁnd the dot product of obtained transpose with the matrices.
4. Similarly repeat these steps to obtain projection matrix P given by P = A * (A * AT) AT

To check which of the matrices cannot be diagonalised 
1. Let A be the n×n matrix that you want to diagonalize. 
2. Find the characteristic polynomial p(t) of A.
3. Find eigenvalues λ of the matrix A and their algebraic multiplicities from the characteristic polynomial p(t).
4. For each eigenvalue λ of A, ﬁnd a basis of the eigenspace Eλ. If there is an eigenvalue λ such that the geometric multiplicity of λ, dim(Eλ), is less than the algebraic multiplicity of λ, then the matrix A is not diagonalizable. If not, A is diagonalizable, and proceed to the next step.
5. If we combine all basis vectors for all eigenspaces, we obtained n linearly independent eigenvectors v1v2...vn.
6. Deﬁne the nonsingular matrix S = [v1v2...vn].
7. Deﬁne the diagonal matrix D, whose (i,i)-entry is the eigenvalue λ such that the i-th column vector vi is in the eigenspace Eλ.
8. Then the matrix A is diagonalized as S−1AS = D.

