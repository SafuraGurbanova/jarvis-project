from datetime import datetime
import memory
import random

def normalize(text):
    return text.lower()\
        .replace("?", "")\
        .replace("ı","i")\
        .replace("ö","o")\
        .replace("ü","u")\
        .replace("ç","c")\
        .replace("ş","s")\
        .replace("ğ","g")\
        .strip()


def cevapla(komut):

    komut = normalize(komut)
    mood = memory.getir("mood")

    responses = {
        "selam": [
            "Selam.",
            "Hey buradayım.",
            "Merhaba Levent."
        ],

        "nasilsin": [
             "İyiyim. Sen nasılsın?",
             "Fena değil. Sen?",
             "Bugün normal moddayım. Sen nasılsın?"
        ]
    }

    if komut in responses:
        print(random.choice(responses[komut]))
        return

    if komut == "saat":
        print(datetime.now().strftime("%H:%M:%S"))
        return

    if komut == "tarih":
        print(datetime.now().strftime("%d.%m.%Y"))
        return

    if komut == "adim ne":
        isim = memory.getir("isim")
        if isim:
            print(f"Adın {isim}.")
        else:
            print("Henüz adını bilmiyorum.")
        return

    if komut.startswith("adim"):
        isim = komut.replace("adim", "").strip()
        if isim:
            memory.kaydet("isim", isim)
            print(f"Tamam {isim}, kaydettim.")
        return

    if "kotu" in komut or "uzgun" in komut:
        memory.kaydet("mood", "sad")
        print("Ne oldu? Anlatmak ister misin?")
        return

    print("Bunu anlayamadım.")
