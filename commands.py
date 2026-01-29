from datetime import datetime
import memory
import random

DEFAULT_STATE = "idle"

FOLLOW_UP = {
    "okul": "Okulda ne oluyor?",
    "aile": "Ailende bir şey mi var?",
    "arkadas": "Arkadaşlarınla mı ilgili?",
    "sinav": "Sınavlar mı yordu seni?"
}

SOLUTIONS = {
    "sinav": [
        "İstersen sınavı küçük parçalara bölelim: bugün sadece 1 konu bak.",
        "25 dakika çalışıp 5 dakika mola vermeyi deneyebilirsin.",
        "Zor gelen dersten değil, kolay olandan başla."
    ],

    "ders": [
        "Bir defter açıp sadece anlamadığın yerleri yazmayı dene.",
        "YouTube’dan kısa konu anlatımı izlemek yardımcı olabilir."
    ],

    "okul": [
        "Belki bugün okuldan sonra kendine küçük bir ödül koyabilirsin.",
        "Her şeyi aynı anda çözmek zorunda değilsin."
    ],

    "aile": [
        "Duygularını biriyle paylaşmak bazen çok rahatlatır.",
        "İstersen biraz yalnız kalıp kafanı toplamak da iyi olabilir."
    ]
}

SUB_PROBLEMS = {
    "okul": {
        "sinav": "Sınavlar mı çok baskı yapıyor?",
        "ogretmen": "Öğretmeninle mi sorun var?",
        "ders": "Dersler mi ağır geliyor?"
    }
}

PROBLEM_WEIGHT = {
    "okul": 1,
    "sinav": 2,
    "ogretmen": 2,
    "ders": 1,
    "aile": 2
}



INTENTS = {
    "greeting": ["selam", "merhaba", "hey"],
    "status": ["nasilsin", "napiyorsun"],
    "time": ["saat"],
    "date": ["tarih"],
    "name_ask": ["adim ne"],
    "name_set": ["adim"],
    "memory_ask": ["az once ne dedim"],
    "reason": ["neden boyleyim"],
    "positive": ["iyiyim", "mutluyum"],
    "negative": ["kotuyum", "uzgunum"]
}

INTENSIFIERS = ["cok", "asiri", "gercekten", "baya"]


def detect_intent(text):
    for intent, words in INTENTS.items():
        for w in words:
            if text.startswith(w) or w in text:
                return intent
    return None



def normalize(text):
    table = str.maketrans("ıöüçşğ", "ioucsg")
    return text.lower().translate(table).replace("?", "").strip()

def cevapla(komut):

    komut = normalize(komut)
    
    intent = detect_intent(komut)
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

    if intent == "status":
        print(random.choice(responses["nasilsin"]))
        return


    if komut not in ["az once ne dedim", "neden boyleyim"]:
        memory.kaydet("last_message", komut)


    state = memory.getir("state")

# neden boyleyim her zaman öncelikli
    if komut == "neden boyleyim":

    # Aynı reflection tekrar edilmesin
        if memory.getir("reason_used"):
            print("Bunu az önce konuştuk. İstersen başka bir yönünden bakalım…")
            return

        problem = memory.getir("last_problem")
        weight = memory.getir("problem_weight") or 0

        if weight >= 3:
            print("Bu seni gerçekten baya yıpratmış gibi görünüyor.")

        if problem:
            print(f"Özellikle {problem} konusu seni zorluyor.")

        if problem in SOLUTIONS:
            print("İstersen şunları deneyebilirsin:")
            for s in SOLUTIONS[problem]:
                print(f"- {s}")
        else:
            print("Bunun nedenini henüz tam anlayamadım.")

        # reflection kilidi
        memory.kaydet("reason_used", True)

        # state reset
        memory.kaydet("state", DEFAULT_STATE)

        return

  
    if state == "waiting_problem":

        parent = memory.getir("last_problem")

        prev = memory.getir("problem_weight") or 0
        memory.kaydet("problem_weight", prev + PROBLEM_WEIGHT.get(komut, 1))



        if parent in SUB_PROBLEMS:
            for sub, q in SUB_PROBLEMS[parent].items():
                if sub in komut:
                    memory.kaydet("last_problem", sub)
                    
                    print(q)
                    return

        if intent != "reason":
           memory.kaydet("last_problem", komut)

        for k, q in FOLLOW_UP.items():
            if k in komut:
                print(q)
                return

        print("Anladım... yanında olmaya çalışırım.")
        return



    
    if intent == "negative":
        level = "normal"

        for i in INTENSIFIERS:
             if i in komut:
                level = "high"

        memory.kaydet("sad_level", level)
        memory.kaydet("state", "waiting_problem")
        memory.kaydet("reason_used", False)

        if level == "high":
          print("Bu bayağı ciddi geliyor… anlatmak ister misin?")
        else:
          print("Ne oldu? Anlatmak ister misin?")
        return




    if komut == "az once ne dedim":
        son = memory.getir("last_message")
        if son:
            print(f"Şunu demiştin: {son}")
        else:
            print("Henüz bir şey söylemedin.")
        return

    if intent == "greeting":
      print(random.choice(responses["selam"]))
      return

    if intent == "time":
        print(datetime.now().strftime("%H:%M:%S"))
        return

    if intent == "date":
        print(datetime.now().strftime("%d.%m.%Y"))
        return

    if intent == "name_ask":
        if isim:
            print(f"Adın {isim}.")
        else:
            print("Henüz adını bilmiyorum.")
        return
    
    if intent == "name_set" and komut != "adim ne":
        isim = komut.replace("adim", "").strip()
        if isim:
         memory.kaydet("isim", isim)
         print(f"Tamam {isim}, kaydettim.")
        return

    if komut == memory.getir("last_problem"):
      print("Bu konu seni gerçekten etkilemiş gibi görünüyor.")
      return

    print("Bunu anlayamadım.")
    return
 