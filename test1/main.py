from math import sqrt
def find_roots(a, b, c):
    ing = sqrt(b*b-4*a*c)
    root_1 = (-b+ing)/(2*a)
    root_2 = (-b-ing)/(2*a)
    return (root_1, root_2)
print(find_roots(2, 10, 8));