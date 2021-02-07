class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
class Rectangle():
    def __init__(self, left_top, right_buttom):
        self.left_top=left_top
        self.right_buttom=right_buttom
        self.w=abs(right_buttom.x-left_top.x)
        self.h=abs(right_buttom.y-left_top.y)
    def area(self):
        return self.w*self.h

        