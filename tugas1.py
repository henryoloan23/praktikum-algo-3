# Henry Oloan Tagor Harahap
# 065002400006

print('======= Selamat Datang di Segitiga Detektor =======')
a = float(input('sisi a = '))
b = float(input('sisi b = '))
c = float(input('sisi c = '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('jenis segitiga: sama sisi')
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print('jenis segitiga: siku - siku')
    else:
        print('jenis segitiga: sembarang')
else:
    print('ini bukan segitiga')
    
print('======= Terima Kasih =======')