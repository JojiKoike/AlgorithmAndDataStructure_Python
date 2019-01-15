from math import pi, cos, sin

th = pi * 60.0 / 180.0

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


def koch(d: int, p1: Point, p2: Point) -> None:
    if d == 0:
        return
    s = Point((p1.x * 2.0 + p2.x * 1.0) / 3.0, (p1.y * 2.0 + p2.y * 1.0) / 3.0)
    t = Point((p1.x * 1.0 + p2.x * 2.0) / 3.0, (p1.y * 1.0 + p2.y * 2.0) / 3.0)
    ux = (t.x - s.x) * cos(th) - (t.y - s.y) * sin(th) + s.x
    uy = (t.x - s.x) * sin(th) + (t.y - s.y) * cos(th) + s.y
    u = Point(ux, uy)
    koch(d - 1, p1, s)
    print("{0} {1}".format(s.x, s.y))
    koch(d - 1, s, u)
    print("{0} {1}".format(u.x, u.y))
    koch(d - 1, u, t)
    print("{0} {1}".format(t.x, t.y))
    koch(d - 1, t, p2)


n = int(input())
p1: Point = Point(0.0, 0.0)
p2: Point = Point(100.0, 0.0)
print("{0} {1}".format(p1.x, p1.y))
koch(n, p1, p2)
print("{0} {1}".format(p2.x, p2.y))
