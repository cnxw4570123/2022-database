import math

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#     def __sub__(self, other):
#         return Point(self.x - other.x, self.y - other.y)
#     def __rmul__(self, other):
#         return Point(self.x * other, self.y * other)
#     def length(self):
#         return math.sqrt(self.x**2 + self.y**2)
#     def dot(self, q):
#         return self.x*q.x + self.y*q.y
#     def getX(self):
#         return self.x
#     def getY(self):
#         return self.y
#     def setX(self, x):
#         self.x = x
#     def setY(self, y):
#         self.y = y

# p = Point(1, 2)
# q = Point(3, 4)
# r = p + q
# s = p.__add__(q)
# t = 3 * q # *연산자 오른쪽이 self, 왼쪽이 other
# print(r, s, t)
# print(r.getX())
# p.setX(10)
# print(p.getX())

class Vector:
    def __init__(self, *args):
        self._coords = list(args) #[x for x in args]
    
    def __str__(self):
        return str(self._coords)

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, k):
        return self._coords[k]

    def __setitem__(self, k, val):
        self._coords[k] = val


v = Vector(1, 2, 3)
# v[-1] = 9

for c in v :
    print(c, end= " ")
    print()