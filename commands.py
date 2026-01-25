from datetime import datetime
import memory
import random

DEFAULT_STATE = "idle"

def normalize(text):
    table = str.maketrans("ıöüçşğ", "ioucsg")
    return text.lower().translate(table).replace("?", "").strip()


def cevapla(komut):
    komut = normalize(komut)

    state = memory.getir("state")
    isim = memory.getir("isim")

    if not state:
        memory.kaydet("state", DEFAULT_STATE)
        state = DEFAULT_STATE

    isim = isim if isim else "dostum"

    if state == "sad":
        memory.kaydet("last_problem", komut)
        memory.kaydet("state", "idle")
        print("Anladım... yanında olmaya çalışırım.")
        return

    responses = {
        "selam": [
            "Selam.",
            "Hey buradayım.",
            f"Merhaba {isim}."
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

    if "iyiyim" in komut:
        print("Buna sevindim 🙂")
        return


    if komut == "saat":
        print(datetime.now().strftime("%H:%M:%S"))
        return

    if komut == "tarih":
        print(datetime.now().strftime("%d.%m.%Y"))
        return

    if komut == "adim ne":
        if isim:
            print(f"Adın {isim}.")
        else:
            print("Henüz adını bilmiyorum.")
        return

    if komut.startswith("adim ") and komut != "adim ne":
        yeni_isim = komut.replace("adim", "").strip()
        if yeni_isim:
            memory.kaydet("isim", yeni_isim)
            print(f"Tamam {yeni_isim}, kaydettim.")
        return

    if "kotu" in komut or "uzgun" in komut:
        memory.kaydet("state", "sad")
        print("Ne oldu? Anlatmak ister misin?")
        return

    memory.kaydet("last_unknown", komut)
    print("Bunu anlayamadım.")
