import random

"""
Kurallar:
* 11 hanelidir.
* Her hanesi rakamsal değer içerir.
* İlk hane 0 olamaz.+
* 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında, elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
* 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
Kurallar http://www.kodaman.org/yazi/t-c-kimlik-no-algoritmasi adresinden alınmıştır.
"""
def isValidTCID(value):
    value = str(value)
    
    # 11 hanelidir.
    if not len(value) == 11:
        return "TC kimlik numaranız 11 haneli olmalıdır."
    
    # Sadece rakamlardan olusur.
    if not value.isdigit():
        return False
    
    # Ilk hanesi 0 olamaz.
    if int(value[0]) == 0:
        return "TC kimlik numaranızın ilk hanesi 0 olamaz."
    
    digits = [int(d) for d in str(value)]
    
    # 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun
    # 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
    if not sum(digits[:10]) % 10 == digits[10]:
        return "Tekrar deneyin."
    
    # 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında,
    # elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return "Tekrar deneyin."
    
    # Butun kontrollerden gecti.
    return("Butun kontrollerden gecti.Giriniz")

x = input("Tc numarınızı giriniz:")
bahar = isValidTCID(x)
print(bahar)