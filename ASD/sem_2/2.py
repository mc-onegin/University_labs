def line_line(line1, line2):
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2
    
    det = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if det == 0:
        return None
    
    px = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / det
    py = ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / det
    
    return (px, py)

def line_segment(line, segment):
    (lx1, ly1), (lx2, ly2) = line
    (sx1, sy1), (sx2, sy2) = segment
    
    det = (lx1-lx2)*(sy1-sy2) - (ly1-ly2)*(sx1-sx2)
    if det == 0:
        return None
    
    px = ((lx1*ly2-ly1*lx2)*(sx1-sx2) - (lx1-lx2)*(sx1*sy2-sy1*sx2)) / det
    py = ((lx1*ly2-ly1*lx2)*(sy1-sy2) - (ly1-ly2)*(sx1*sy2-sy1*sx2)) / det
    
    if (min(sx1, sx2) <= px <= max(sx1, sx2) and 
        min(sy1, sy2) <= py <= max(sy1, sy2)):
        return (px, py)
    return None

def segment_segment(seg1, seg2):
    (x1, y1), (x2, y2) = seg1
    (x3, y3), (x4, y4) = seg2
    
    det = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if det == 0:
        return None
    
    px = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / det
    py = ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / det
    
    if (min(x1, x2) <= px <= max(x1, x2) and 
        min(y1, y2) <= py <= max(y1, y2) and
        min(x3, x4) <= px <= max(x3, x4) and 
        min(y3, y4) <= py <= max(y3, y4)):
        return (px, py)
    return None

def line_circle(line, circle):
    (lx1, ly1), (lx2, ly2) = line
    (cx, cy), r = circle
    
    A = ly2 - ly1
    B = lx1 - lx2
    C = lx2*ly1 - lx1*ly2
    
    dist = abs(A*cx + B*cy + C) / (A**2 + B**2)**0.5
    
    if dist > r:
        return []
    elif abs(dist - r) < 10**-5:
        t = (A*cx + B*cy + C) / (A*A + B*B)
        x0 = cx - A*t
        y0 = cy - B*t
        return [(x0, y0)]
    else:
        d = (r**2 - dist**2)**0.5
        vx = lx2 - lx1
        vy = ly2 - ly1
        length = (vx**2 + vy**2)**0.5
        vx /= length
        vy /= length
        
        x0 = cx - dist * (A / (A**2 + B**2)**0.5)
        y0 = cy - dist * (B / (A**2 + B**2)**0.5)
        
        p1 = (x0 + d * vx, y0 + d * vy)
        p2 = (x0 - d * vx, y0 - d * vy)
        return [p1, p2]
    
def segment_circle(segment, circle):
    (sx1, sy1), (sx2, sy2) = segment
    (cx, cy), r = circle
    
    line = line_circle(segment, circle)
    
    result = []
    for (px, py) in line:
        if (min(sx1, sx2) <= px <= max(sx1, sx2) and 
            min(sy1, sy2) <= py <= max(sy1, sy2)):
            result.append((px, py))
    
    return result

def circle_circle(circle1, circle2):
    (x1, y1), r1 = circle1
    (x2, y2), r2 = circle2
    
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    if d > r1 + r2 or d < abs(r1 - r2):
        return []
    elif d == 0 and r1 == r2:
        return []
    elif abs(d - (r1 + r2)) < 10**-5 or abs(d - abs(r1 - r2)) < 10**-5:
        a = (r1**2 - r2**2 + d**2) / (2*d)
        h = (r1**2 - a**2)**0.5
        
        x3 = x1 + a*(x2 - x1)/d
        y3 = y1 + a*(y2 - y1)/d
        
        return [(x3, y3)]
    else:
        a = (r1**2 - r2**2 + d**2) / (2*d)
        h = (r1**2 - a**2)**0.5
        x3 = x1 + a*(x2 - x1)/d
        y3 = y1 + a*(y2 - y1)/d
        
        x4 = x3 + h*(y2 - y1)/d
        y4 = y3 - h*(x2 - x1)/d
        
        x5 = x3 - h*(y2 - y1)/d
        y5 = y3 + h*(x2 - x1)/d
        
        return [(x4, y4), (x5, y5)]
    
def point_in_triangle(p, triangle):
    (x1, y1), (x2, y2), (x3, y3) = triangle
    px, py = p
    
    det = ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    if det == 0:
        return False
    
    a = ((y2 - y3)*(px - x3) + (x3 - x2)*(py - y3)) / det
    b = ((y3 - y1)*(px - x3) + (x1 - x3)*(py - y3)) / det
    c = 1 - a - b
    
    return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1

def is_triangle_inside(tri1, tri2):
    for point in tri1:
        if not point_in_triangle(point, tri2):
            return False
    return True

def find_triangles(points):
    n = len(points)
    
    triangles = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                triangles.append((points[i], points[j], points[k]))
    
    for i in range(len(triangles)):
        for j in range(i+1, len(triangles)):
            if is_triangle_inside(triangles[i], triangles[j]):
                return True, triangles[j], triangles[i]
            if is_triangle_inside(triangles[j], triangles[i]):
                return True, triangles[i], triangles[j]
    
    return False, None, None
    

# Тест 1: line_line
print("1. line_line:")
# Прямые: y=x и y=2-x
line1 = ((0,0), (1,1))
line2 = ((0,2), (2,0))
print("  + Пересечение в (1,1):", line_line(line1, line2))

# Параллельные прямые y=0 и y=1
line3 = ((0,0), (1,0))
line4 = ((0,1), (1,1))
print("  - Параллельные:", line_line(line3, line4))  # None

# Тест 2: line_segment
print("\n2. line_segment:")
# Прямая y=x, отрезок (0,0)-(2,2)
line = ((0,0), (1,1))
segment = ((2,0), (2,2))
print("  + Пересечение в (0,0):", line_segment(line, segment))  # (0.0, 0.0)

# Прямая y=x, отрезок (0,1)-(1,0) (пересекает, но не на прямой)
line = ((0,0), (1,1))
segment = ((0,1), (0.25,1))
print("  - Не пересекает прямую:", line_segment(line, segment))  # None

# Тест 3: segment_segment
print("\n3. segment_segment:")
seg1 = ((0,0), (2,2))
seg2 = ((0,2), (2,0))
print("  + Пересечение в (1,1):", segment_segment(seg1, seg2))  # (1.0, 1.0)

# Параллельные отрезки
seg3 = ((0,0), (2,0))
seg4 = ((0,1), (2,1))
print("  - Параллельные:", segment_segment(seg3, seg4))  # None

# Тест 4: line_circle
print("\n4. line_circle:")
circle = ((0,0), 5)
line = ((0,3), (1,3))
print("  + Две точки пересечения:", line_circle(line, circle))  # [(-4.0, 3.0), (4.0, 3.0)]

circle2 = ((0,0), 3)
line2 = ((0,5), (1,5))
print("  - Нет пересечения:", line_circle(line2, circle2))  # []

# Тест 5: segment_circle
print("\n5. segment_circle:")
circle = ((0,0), 5)
segment = ((-2.0,5.0), (5.0,5.0))
print("  + точка касания:", segment_circle(segment, circle))  # [(0, 5)]

segment2 = ((0,6), (4,6))
print("  - Нет пересечения:", segment_circle(segment2, circle))  # []

# Тест 6: circle_circle
print("\n6. circle_circle:")
circle1 = ((0,0), 5)
circle2 = ((6,0), 5)
print("  + Две точки пересечения:", circle_circle(circle1, circle2))  # [(3.0, -4.0), (3.0, 4.0)]

circle3 = ((0,0), 2)
circle4 = ((10,0), 3)
print("  - Нет пересечения:", circle_circle(circle3, circle4))  # []

# Тест 7: is_triangle_inside
print("\n7. is_triangle_inside:")
big_tri = ((0,0), (6,0), (3,6))
small_tri = ((2,1), (4,1), (3,2))
print("  + Малый внутри большого:", is_triangle_inside(small_tri, big_tri))  # True

tri1 = ((0,0), (2,0), (1,2))
tri2 = ((3,0), (5,0), (4,2))
print("  - Отдельные треугольники:", is_triangle_inside(tri1, tri2))  # False

# Тест 8: find_triangles
print("\n8. find_triangles:")
points = [(0,0), (2,1), (4,1), (6,0), (3,6), (3,2)]
found, outer, inner = find_triangles(points)
print("  + Есть вложенные:", found)
if found:
    print("    Внешний:", outer)
    print("    Внутренний:", inner, end="\n\n")

points2 = [(0,0), (2,-1), (5,0), (4,2)]
found2, outer2, inner2 = find_triangles(points2)
print("  - Вложенность:", found2)