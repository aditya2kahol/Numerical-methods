"""
Gauss-Jacobi's method
Author: Aditya Kahol

Caution: 1)Diagonally dominant matrices must be used in this.
         2)It is assumed that numpy matrices(arrays) are used for input A.
         3)List is used for input b.

Input: A 3x3 Diagonally dominant matrix A, vector b, initial guesses x,y and z, and number of iterations required n.
Output: n iterations for the approximate soln, final one being the solution of the system Ax = b.
"""
import numpy as np

def gj(A,b,x,y,z,n):
    # A -> numpy matrix, b -> list.
    for i in range(3):
        if np.abs(A[i,i]) < np.abs(np.sum(A[i])) - np.abs(A[i,i]):
            print("Matrix A is not diagonally dominant")
            quit()
    k = 0
    while True:
        p = (1/A[0,0])*( b[0] - A[0,1]*y - A[0,2]*z )
        q = (1/A[1,1])*( b[1] - A[1,0]*x - A[1,2]*z )
        r = (1/A[2,2])*( b[2] - A[2,0]*x - A[2,1]*y )
        x,y,z = (p,q,r)
        k += 1
        if k <= n:
            print("Iteration",str(k)+":","x =",x,"y =",y,"z =",z)
        else:
            break
