import json

def urun_ekle(isim, id, price):
    try:
        with open("IDFinder.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"items": []}
    except json.JSONDecodeError:
        print("JSON dosyası bozuk, yeni bir dosya oluşturuluyor.")
        data = {"items": []}

    urun = {"isim": isim, "numara": id, "fiyat": price}
    data["items"].append(urun)

    with open("IDFinder.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"{isim} ürünü başarıyla eklendi.")

def urun_bul(numara):
    try:
        with open("IDFinder.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Veri dosyası bulunamadı.")
        return None
    except json.JSONDecodeError:
        print("Veri dosyası bozuk.")
        return None

    for urun in data["items"]:
        if urun["numara"] == numara:
            return urun
    return None

def main():
    while True:
        print("\nStok Programı")
        print("1. Ürün Ekle")
        print("2. Ürün Bul")
        print("3. Çıkış")

        secim = input("Bir seçenek girin: ")

        if secim == "1":
            isim = input("Ürün ismini girin: ")
            try:
                numara = int(input("Ürün numarasını girin: "))
                fiyat = float(input("Ürün fiyatını girin: "))
                urun_ekle(isim, numara, fiyat)
            except ValueError:
                print("Lütfen geçerli bir numara ve fiyat girin.")

        elif secim == "2":
            try:
                numara = int(input("Bulmak istediğiniz ürün numarasını girin: "))
                urun = urun_bul(numara)
                if urun:
                    print(f"Ürün Bulundu: İsim: {urun['isim']}, Numara: {urun['numara']}, Fiyat: {urun['fiyat']}")
                else:
                    print("Ürün bulunamadı.")
            except ValueError:
                print("Geçerli bir numara girin.")

        elif secim == "3":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
