"""
Regula falsi method
Author: Aditya Kahol
"""
#Input: a lambda function f, lower limit 'a', upper limit 'b', no. of approx. 'n'
#Output: All the approximations.

def rf(f,a,b,n):
    if f(a)*f(b) > 0:
        print("Try again with different values of 'a' and 'b'")
    else:
        a = min([a,b])
        b = max([a,b])
        i = 0
        while True:
            x = a - ( f(a)/(f(b) - f(a)) )*( b - a )
            i = i + 1
            print("Approximation",str(i)+")","for x = ",x,"f(x):",f(x))
            if i == n:
                break
            
            if f(a)*f(x) <= 0:
                b = x
            else:
                a = x
