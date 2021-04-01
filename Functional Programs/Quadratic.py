from cmath import sqrt
def calucalte_roots(a, b, c):
    delta = pow(b,2) - (4*a*c)          # delta = b*2 - 4*a*c
    root1 = (-b + sqrt(delta))/(2*a)    # Root 1 of x = (-b + sqrt(delta))/(2*a)
    root2 = (-b - sqrt(delta))/(2*a)    # Root 2 of x = (-b - sqrt(delta))/(2*a)
    print("The roots are {} and {}".format(root1, root2))

print("The Quadratic Equation a*x*x + b*x + c")
a = int(input("Enter 'a': "))
b = int(input("Enter 'b': "))
c = int(input("Enter 'c': "))
calucalte_roots(a,b,c)