string = input()
test = string.replace(" ", "").replace("-",  "")
if test.isdigit():
    a, b, c = map(float, string.split())
    if a == 0:
        print(-c / b)
    else:
        D = b ** 2 - (4 * a * c)
        x_1 = (-b + D ** 0.5) / (2 * a)
        x_2 = (-b - D ** 0.5) / (2 * a)
        print(f'x_1 = {x_1}')
        print(f'x_2 = {x_2}')
else:
    print("Мне нужны числа!")


