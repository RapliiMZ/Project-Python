import random

min_num = 1
max_num = 10
sect_num = random.randint(min_num, max_num)

tebak = int(input('tebak angka 1 sampai dengan 10: '))

while tebak != sect_num:
    if tebak < sect_num:
        print ('angka anda kurang besar')
    else :
        print ('angka anda terlalu besar')

    tebak = int(input('coba lagi: '))

print ('tebakan anda benerr cuy...')