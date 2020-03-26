import re

def hepsiASCIIMi(dizge):
    return all(ord(k) < 128 for k in dizge)

def ePostaGeçerliMi(adres):
    if re.match("\\A(?P<name>[\\w\\-_]+)@(?P<domain>[\\w\\-_]+).(?P<toplevel>[\\w]+)\\Z",adres,re.IGNORECASE):
        if (hepsiASCIIMi(adres)):
            return True
        else:
            return False 
    return False
    
def main():
    email = input("Lütfen bir E-posta adresi giriniz: ")

    if (ePostaGeçerliMi(email)):
        print("Adresiniz geçerlidir.")
    else:
        print("Geçersiz adres.")

if __name__ == "__main__":
    main()

print("Diğer işleme geçiyoruz.")

kullanıcı_şifre = input("Şifrenizi yazın: ")

print("Şifrenizi yazdığınız için teşekkürler artık hacklenmeye hazır olun :)")
