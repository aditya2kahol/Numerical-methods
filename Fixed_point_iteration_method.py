"""
Fixed point iteration method
Author: Aditya Kahol
"""
"""
Input: functions-> 'phi', initial approx-> x0, and n
Ouput: n iterations of the root.

Caution: Choose the function 'phi', such that |d_phi(x)| < 1, otherwise the method won't work. 
"""

def fpim(phi,x0,n):
    i = 0
    while True:
        xn = phi(x0)
        i = i + 1
        x0 = xn
        print("Iteration",str(i)+") x =",xn)
        if i == n:
            break
