# Вычисление площади
# a, b- длина сторон, м
# return- 0, если стороны меньше 0
def Square_Rectangle (a, b):
    if a<0 or b<0:
        return 0
    else:
        return a*b
