a,b,c=input().split()
def f():
    try:
        float(a)
        float(b)
        float(c)
        return True
    except ValueError:
        return False
if f():
    a=int(a); b=int(b); c=int(c)
    d = (b**2 - 4*a*c)**1/2
    if d>0 and a!=0:
        x1 = ((-b) - d)/(2*a)
        x2 = ((-b) + d)/(2*a)
        print(x1, x2)
    elif d==0 and a!=0:
        x=(-b)/2*a
        print(x)
    else:
        print('Нет корней')
else:
    print('Введите числa')