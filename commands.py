from datetime import datetime
import memory
import random

DEFAULT_STATE = "idle"


def normalize(text):
    table = str.maketrans("ıöüçşğ", "ioucsg")
    return text.lower().translate(table).replace("?", "").strip()

def cevapla(komut):

    komut = normalize(komut)

    if komut not in ["az once ne dedim", "neden boyleyim"]:
        memory.kaydet("last_message", komut)


    state = memory.getir("state")

    if state == "waiting_problem":
      memory.kaydet("last_problem", komut)
      memory.kaydet("state", DEFAULT_STATE)
      print("Anladım... yanında olmaya çalışırım.")
      return
    
    if "kotu" in komut or "uzgun" in komut:
        memory.kaydet("state", "waiting_problem")
        print("Ne oldu? Anlatmak ister misin?")
        return


    isim = memory.getir("isim")

    responses = {
        "selam": [
            "Selam.",
            "Hey buradayım.",
            f"Merhaba {isim if isim else 'dostum'}."
        ],
        "nasilsin": [
            "İyiyim. Sen nasılsın?",
            "Fena değil. Sen?",
            "Bugün normal moddayım. Sen nasılsın?"
        ],
        "iyiyim": [
            "Buna sevindim 🙂",
            "Güzel, böyle devam.",
            "İyi olmana sevindim."
        ],

    }

    if komut == "az once ne dedim":
        son = memory.getir("last_message")
        if son:
            print(f"Şunu demiştin: {son}")
        else:
            print("Henüz bir şey söylemedin.")
        return
    
    if "kotu" in komut or "uzgun" in komut:
      memory.kaydet("state", "waiting_problem")
      print("Ne oldu? Anlatmak ister misin?")
      return


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
        if isim:
            print(f"Adın {isim}.")
        else:
            print("Henüz adını bilmiyorum.")
        return

    if komut.startswith("adim ") and komut != "adim ne":
        isim = komut.replace("adim", "").strip()
        if isim:
            memory.kaydet("isim", isim)
            print(f"Tamam {isim}, kaydettim.")
        return

    if komut == "neden boyleyim":
       problem = memory.getir("last_problem")

       if problem:
            print(f"Sanırım {problem} yüzünden böyle hissediyorsun.")
            print("İstersen biraz anlatabilirsin ya da mola vermeyi deneyebilirsin.")
       else:
            print("Bunun nedenini henüz bilmiyorum.")
       return

    if komut == memory.getir("last_problem"):
      print("Bu konu seni gerçekten etkilemiş gibi görünüyor.")
      return

    memory.kaydet("last_message", komut)
    print("Bunu anlayamadım.")
    return
