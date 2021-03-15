"""
Bisection method
"""
# input: function f, and values in abscissa, such that f(a).f(b) < 0, and an error term e.
# ouput: root of f, lying in (a,b).

def bm(f,a,b,e):
    a = min([a,b])
    b = max([a,b])
    
    if f(a)*f(b) > 0:
        print("Wont work for these values of a and b")
        quit()
    else:
        while True:
            c = (a + b)/2
            if f(a)*f(c) < 0:
                a,b = (a,c)
            else:
                a,b = (c,b)
            if b-a < e:
                break

    root = (a+b)/2
    print("Root of f, according to bisection method is:",root)
