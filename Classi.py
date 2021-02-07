from Point import Point, Rectangle

A=Point(10, 20)
C=Point(15,37)
R=Rectangle(A,C)
print(R.w)
print(R.h)
print(R.area())

A2=Point(22, 45)
C2=Point(43,80)
R2=Rectangle(A2,C2)
print(R2.w)
print(R2.h)
print(R2.area())