
word = ["zero","one","two","three","four","five","six","seven","eight","nine"]

#10,11,12,13,15 = beda sendiri
#14,16.....19 = angka belakang + teen
#20,30,40........90 = puluhan beda sendiri
#21,22 = twenty + angka belakang
#100 = bilangan depan + hundred
#101 = bilangan depan + and + bilangan belakang
#1000 = bilangan awal + thousand
#1001 = bilangan awal +  bilangan belakang

def terbilang(n):
    if n < 10:
        return word[n]
    elif n >= 1_000_000_000 :
        return terbilang(n // 1_000_000_000) + ' billion ' + (terbilang(n % 1000000000) if (n % 1000000000 != 0) else "")
    elif n >= 1_000_000 :
        return terbilang(n // 1_000_000) + ' million ' + (terbilang(n % 1000000) if (n % 1000000 != 0) else "")
    elif n >= 1000 and n <= 999999 :
       return terbilang(n // 1000) + ' thousand ' + (terbilang(n % 1000) if (n % 1000 != 0) else "")
    elif n >= 100:
        return terbilang(n // 100) + ' hundred' + (' and ' if n % 100 != 0 else '') + (terbilang(n % 100) if n % 100 != 0 else '')
    elif n > 60 and n <= 99:
        return terbilang(n // 10) + 'ty ' + (terbilang(n % 10) if (n % 10 != 0) else "")
    elif n >=60 :
        return 'sixty'+ (terbilang(n % 10) if (n % 10 != 0) else "")
    elif n >=50 :
        return 'fifty'+ (terbilang(n % 10) if (n % 10 != 0) else "")
    elif n >=40 :
        return 'forty'+ (terbilang(n % 10) if (n % 10 != 0) else "")
    elif n >=30 :
        return 'thirty'+ (terbilang(n % 10) if (n % 10 != 0) else "")
    elif n >=20 :
        return 'twenty'+ (terbilang(n % 10) if (n % 10 != 0) else "")
    elif n == 10:
        return 'Ten'
    elif n == 11:
        return 'Eleven'
    elif n == 12:
        return 'Twelve'
    elif n == 13:
        return 'Thirteen'
    elif n == 15:
        return 'Fifteen'
    else: 
        return terbilang(n % 10) + 'teen'



import os
while True:
    os.system('cls')
    try:
        n = int(input("Insert integer   ?"))
        print(f'{n} : {terbilang(n)} ')
    except:
        print("Only integer bro...")
    os.system('pause')


