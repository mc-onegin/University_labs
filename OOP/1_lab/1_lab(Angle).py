import math
from typing import Self

class Angle:
    def __init__(self, value) -> None:
        self.radians = value

    @classmethod
    def from_degrees(cls, degrees: float) -> Self:
        return cls(degrees * math.pi / 180)


    def normal(self, radians) -> Self:
        normalized = radians % (2 * math.pi)
        if normalized < 0:
            normalized += 2 * math.pi
        return normalized
    
    @property
    def radians(self) -> float:
        return self._radians
    
    @radians.setter
    def radians(self, value: int | float) -> None:
        self._radians = value

    @property
    def degrees(self) -> float:
        return (self._radians * 180 / math.pi)
    
    @degrees.setter
    def degrees(self, value: int | float) -> None:
        self._radians = value * math.pi / 180

    # region magic methods

    def __eq__(self, other: Self) -> bool:
        return math.isclose(self.normal(self.radians), self.normal(other.radians))
    
    def __le__(self, other: Self) -> bool:
        return self.normal(self.radians) <= self.normal(other.radians)
    
    def __lt__(self, other: Self) -> bool:
        return self.normal(self.radians) < self.normal(other.radians)
    def __ge__(self, other: Self) -> bool:
        return self.normal(self.radians) >= self.normal(other.radians)
    def __gt__(self, other: Self) -> bool:
        return self.normal(self.radians) > self.normal(other.radians)
    def __ne__(self, other: Self) -> bool:
        return not(self.__eq__(other))
    
    # endregion
    
    def __int__(self):
        return int(self.radians)
    
    def __float__(self):
        return float(self.radians)
    
    def __str__(self):
        return str(self.radians)
    
    def __repr__(self):
        return f"Angle: {self.radians}"
    
    def __add__(self, other: Self | float | int) -> Self:
        if isinstance(other, (int, float)):
            return Angle(self.radians + other)
        return Angle(self.radians + other.radians)
    
    def __radd__(self, other: float | int) -> Self:
        return self.__add__(other)
    
    def __sub__(self, other: Self | float | int) -> Self:
        if isinstance(other, (int, float)):
            return Angle(self.radians - other)
        return Angle(self.radians - other.radians)
    
    def __rsub__(self, other: float | int) -> Self:
        return Angle(other - self.radians)
    
    def __mul__(self, other: float | int) -> Self:
        if isinstance(other, (int, float)):
            return Angle(self.radians * other)
        return NotImplemented
    
    def __rmul__(self, other: float | int) -> Self:
        return self.__mul__(other)
    
    def __truediv__(self, other: float | int) -> Self:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Error: Division by zero")
            return Angle(self.radians / other)
        return NotImplemented
    
    def __rtruediv__(self, other: float | int) -> Self:
        if self.radians == 0:
            raise ZeroDivisionError("Error: Division by zero")
        return self.__truediv__(other / self.radians)
    

class AngleRange:
    def __init__(self, start: float | int, 
                 end: float | int, 
                 start_include: bool = True, 
                 end_include: bool = True) -> None:
        self.start = start
        self.end = end
        self.start_include = start_include
        self.end_include = end_include

    def range_from_angles(cls, start: Angle, 
                          end: Angle, 
                          start_include: bool = True, 
                          end_include: bool = True) -> Self:
        return cls(start, end, start_include, end_include)
    
    def __abs__(self) -> float:
        if self.end >= self.start:
            return self.end - self.start
        else:
            return (2 * math.pi - self.start) + self.end
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AngleRange):
            return False
        return (self.start == other.start and 
                self.end == other.end and 
                self.start_include == other.start_include and 
                self.end_include == other.end_include)
        
    def __lt__(self, other: Self) -> bool:
        return self.__abs__() < other.__abs__()
    
    def __le__(self, other: Self) -> bool:
        return self.__abs__ <= other.__abs__
    
    def __gt__(self, other: Self) -> bool:
        return self.__abs__ > other.__abs__
    
    def __ge__(self, other: Self) -> bool:
        return self.__abs__ >= other.__abs__
    
    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)
    
    def __contains__(self, other: Self | Angle | float | int) -> bool:
        if isinstance(other, (int, float)):
            other = Angle(other)
        
        if isinstance(other, Angle):
            start_angle = self.start if isinstance(self.start, Angle) else Angle(self.start)
            end_angle = self.end if isinstance(self.end, Angle) else Angle(self.end)
            angle_rad = other.radians
            start_rad = start_angle.radians
            end_rad = end_angle.radians
            
            if start_rad <= end_rad:
                start_ok = angle_rad > start_rad or (self.start_include and angle_rad == start_rad)
                end_ok = angle_rad < end_rad or (self.end_include and angle_rad == end_rad)
                return start_ok and end_ok
            else:
                in_first = angle_rad >= start_rad or (self.start_include and angle_rad == start_rad)
                in_second = angle_rad <= end_rad or (self.end_include and angle_rad == end_rad)
                return in_first or in_second
        
        elif isinstance(other, AngleRange):
            return (other.start in self and other.end in self)
        
        return False
    
    def __repr__(self) -> str:
        start_bracket = '[' if self.start_include else '('
        end_bracket = ']' if self.end_include else ')'
        return f"AngleRange: {start_bracket}{self.start}, {self.end}{end_bracket}"
    
    def __str__(self) -> str:
        start_bracket = '[' if self.start_include else '('
        end_bracket = ']' if self.end_include else ')'
        return f"{start_bracket}{self.start}, {self.end}{end_bracket}"
    
    def __add__(self, other: Self) -> Self:
        
        intersects = (other.start in self or other.end in self or 
                     self.start in other or self.end in other)
        
        near = ((self.end == other.start and (self.end_include or other.start_include)) or
                   (other.end == self.start and (other.end_include or self.start_include)))
        
        if intersects or near:
            new_start = min(self.start, other.start)
            new_end = max(self.end, other.end)
            
            if self.start == other.start:
                new_start_include = self.start_include or other.start_include
            else:
                new_start_include = self.start_include if self.start == new_start else other.start_include
            
            if self.end == other.end:
                new_end_include = self.end_include or other.end_include
            else:
                new_end_include = self.end_include if self.end == new_end else other.end_include
            
            return AngleRange(new_start, new_end, new_start_include, new_end_include)
        else:
            if self.start < other.start:
                return [self, other]
            else:
                return [other, self]
            
    def __sub__(self, other: Self) -> Self:
        intersects = (other.start in self or other.end in self or 
                     self.start in other or self.end in other)

        if not intersects:
            return [self]
        
        result = []
        
        if self.start < other.start or (self.start == other.start and self.start_include and not other.start_include):
            left_end = other.start
            left_end_include = not other.start_include        
            if self.start < left_end or (self.start == left_end and self.start_include and left_end_include):
                result.append(AngleRange(self.start, left_end, self.start_include, left_end_include))
        
        if self.end > other.end or (self.end == other.end and self.end_include and not other.end_include):
            right_start = other.end
            right_start_include = not other.end_include   
            if right_start < self.end or (right_start == self.end and right_start_include and self.end_include):
                result.append(AngleRange(right_start, self.end, right_start_include, self.end_include))
        
        return result if result else None


print("1. ТЕСТЫ Angle:")

angle1 = Angle(math.pi)
print(f"angle1 (π rad) = {angle1} rad | ОЖИДАЕМО: 3.14 radians")

angle2 = Angle.from_degrees(90)
print(f"angle2 (90°) = {angle2} rad | ОЖИДАЕМО: 1.57 radians")

angle3 = Angle.from_degrees(360)
angle4 = Angle.from_degrees(0)
print(f"angle3: {angle3} rad | ОЖИДАЕМО: 6.28 rad")
print(f"angle4: {angle4} rad | ОЖИДАЕМО: 0 rad")
print(f"360° == 0°: {angle3 == angle4} | ОЖИДАЕМО: True")

result1 = Angle.from_degrees(120) + Angle.from_degrees(90)
print(f"120° + 90° = {result1} rad | ОЖИДАЕМО: примерно 3.66519 rad")

result2 = Angle.from_degrees(150) - Angle.from_degrees(93)
print(f"150° - 93° = {result2} rad | ОЖИДАЕМО: примерно 1 rad")
result3 = 3 * Angle.from_degrees(57)
print(f"3 * 57° = {result3} rad | ОЖИДАЕМО: примерно 3 Rad")
print(f"angle1 (π rad) / 3 = {angle1 / 3} rad | ОЖИДАЕМО: примерно 1.05 rad")

print("\n2. ТЕСТЫ AngleRange:")

range1 = AngleRange(0, 90, start_include=False)
print(f"range1 (0°,90°] = {range1} | ОЖИДАЕМО: (0, 90]")

print(f"Длина range1: {abs(range1)} deg | ОЖИДАЕМО: 90°")

angle5 = Angle.from_degrees(45)
print(f"45 deg в range1: {angle5 in range1} | ОЖИДАЕМО: True")


range2 = AngleRange(45, 180, start_include = False, end_include = False)
result3 = range1 + range2
print(f"(0°,90°] + (45°,180°) = {result3} | ОЖИДАЕМО: (0, 180)")

result4 = range1 - range2
print(f"(0°,90°] - (45°,180°) = {result4} | ОЖИДАЕМО: (0, 45]")

range3 = AngleRange(Angle(math.pi/2), Angle(math.pi * 3 / 2))
range4 = AngleRange(Angle(math.pi), Angle(math.pi * 5 / 4))
print(f"range4 [π, 5π/4] in range3[π/2, 3π/2]: {range4 in range3} | Ожидаемо: True")
range5 = AngleRange(10, 40)
range6 = AngleRange(10, 40, start_include = False, end_include = False)
print(f"range5: [10, 40] - range6: (10, 40): {range5 - range6} | Ожидаемо: [10, 10], [40, 40]")
