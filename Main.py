import Func as f

a=int(input("Введите сторону A: "))
b=int(input("Введите сторону B: "))
c= f.Square_Rectangle(a,b)
if c==0:
    print("Error: a or b less 0")
    exit(0)
print(c)
