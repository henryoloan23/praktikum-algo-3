# Henry Oloan Tagor Harahap
# 065002400006
import math
a = int(input('masukkan nilai A = '))
b = int(input('masukkan nilai B = '))
c = int(input('masukkan nilai C = '))
diskriminan = (b ** 2) - (4 * a * c)

print('persamaan kuadrat: ' ,a, 'x^2 + ', b, 'x + ', c )
print('Diskriminan: ', diskriminan)

if (diskriminan == 0):
    x = -b / (2 * a)
    print('Merupakan akar kembar')
    print('akar= ',x)
elif (diskriminan > 0):
    x1 = (-b + math.sqrt(diskriminan)) / (2 * a)
    x2 = (-b - math.sqrt(diskriminan)) / (2 * a)
    print('Merupakan akar yang berbeda')
    print('x1 = ', x1)
    print('x2 = ', x2)
else:
    print('merupakan akar imajiner')
    print('x1 = ', (-b + math.sqrt(diskriminan)) / (2 * a))
    print('x2 = ', (-b - math.sqrt(diskriminan)) / (2 * a))