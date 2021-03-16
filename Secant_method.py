"""
Secant method
Author: Aditya Kahol
"""
# input: function f, two approximations of the root a & b, no. of iterations n
# output: all n iterations for f.

def sm(f,a,b,n):
    a,b = sorted((a,b))
    if f(a) == f(b):
        print("Change the values of a and b")
        quit()
    else:
        i = 0
        while True:
            xn = b - (f(b)*(b - a))/(f(b) - f(a))
            i = i + 1
            a,b = (b,xn)
            if f(a) - f(b) == 0:
                break

            print("Iteration",str(i)+") x =",xn,"| f(x) =",f(xn))

            if i == n:
                break
