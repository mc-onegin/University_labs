import math

def vect_mult(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def polar_angle(start, p):
    return math.atan2(p[1] - start[1], p[0] - start[0])

def graham(points, n):
    if n < 3:
        return []
    
    start = min(points, key=lambda p: (p[1], p[0]))
    points.sort(key=lambda p: polar_angle(start, p))
    
    shell = [start]
    for p in points[1:]:
        while len(shell) > 1 and vect_mult(shell[-2], shell[-1], p) <= 0:
            shell.pop()
        shell.append(p)
    
    return shell

n = int(input("input number of dots: "))
print("input dots")
points = [tuple(map(int, input().split())) for i in range(n)]

shell = graham(points, n)

if len(shell) >= 3:
    print("true")
    print(shell)
else:
    print("false")