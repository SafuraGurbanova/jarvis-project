from datetime import datetime
import memory

def cevapla(komut):
    if komut == "selam":
        print("Selam.")

    elif komut == "nasilsin":
        print("İyiyim. Sen nasılsın?")

    elif komut == "tarih":
        print(datetime.now().strftime("%d.%m.%Y"))

    elif komut == "saat":
        print(datetime.now().strftime("%H:%M:%S"))

    elif komut == "adim ne":
        isim = memory.getir("isim")
        if isim:
            print(f"Adın {isim}.")
        else:
            print("Adını henüz bilmiyorum.")

    elif komut.startswith("adim"):
        isim = komut.replace("adim", "").strip()
        if isim:
            memory.kaydet("isim", isim)
            print(f"Tamam, adını kaydettim: {isim}")
        else:
            print("Adını söylemedin.")

    else:
        print("Bunu anlayamadım.")
