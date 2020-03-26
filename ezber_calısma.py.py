yazar_eser = {
    "Muharrir Bu Ya" : "Ahmet Rasim",
    "Edebiyat Söyleşiler": "Suut Kemal",
    "İt Ürür Kervan Yürür": "Nazım Hikmet",
    "Eğil Dağlar": "Yahya Kemal",
    "Deve Kuşuna Mektuplar": "Haldun Taner",
    "Çile": "Falih Rıfkı Atay",
    "Ramazan Sohbetleri": "Ahmet Rasim",
}

while True:
    raw = input("'Muharrir Bu Ya' adlı eser kime aittir: ")
    if raw == yazar_eser["Muharrir Bu Ya"]:
        print("Doğru") 
        raw = input("'Edebiyat Söyleşiler' adlı eser kime aittir: ")
        if raw == yazar_eser["Edebiyat Söyleşiler"]:
            print("Doğru")
            raw = input("'İt Ürür Kervan Yürür' adlı eser kime aittir: ")
            if raw == yazar_eser["İt Ürür Kervan Yürür"]:
    	        print("Doğru")

    raw = input("'Eğil Dağlar' adlı eser kime aittir: ")
    if raw == yazar_eser["Eğil Dağlar"]:
    	print("Doğru")
    raw = input("'Deve Kuşuna Mektuplar' adlı eser kime aittir: ")	
    if raw == yazar_eser["Deve Kuşuna Mektuplar"]:
    	print("Doğru")
