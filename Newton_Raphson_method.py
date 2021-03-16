"""
Newton-Raphson method
Author: Aditya Kahol
"""
"""
input: function f, its derivation f_dash and a point x0, and n
output: total iterations
"""

def nrm(f,f_dash,x0,n):
    i = 0
    while True:
        if f_dash(x0) == 0:
            print("Cant apply this method")
            quit()
        else:
            xn = x0 - f(x0)/f_dash(x0)
            i = i + 1
            x0 = xn
            print("Iteration",str(i)+") x = ",x0,"f(x):",f(x0))
            if i == n:
                break
