from random import randint

rand = randint(2,23)
print(rand)
print(""" 
Kurallar:
>>> Eğer 0'a basarsınız oyunu iptal edersiniz.
>>> Eğer 1'e basarsanız pes edersiniz.
""")
while True :
    sayı = int(input("Sayı giriniz: "))
    if (sayı == 0 ):
        print("Oyunu iptal ediniz.")
        break
    elif sayı == 1:
        print("Pes ettiniz :( Sayı {}".format(rand))
    elif sayı < rand:
        print("Daha yüksek sayı giriniz.")
        continue 
    elif sayı > rand:
        print("Daha düşük sayı giriniz.")
        continue    
    else : 
        print("Doğru sayı girdiniz. Sayı {}.".format(rand))
        break