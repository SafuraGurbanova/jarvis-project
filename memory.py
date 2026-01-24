hafiza = {}

def kaydet(anahtar, deger):
    hafiza[anahtar] = deger

def getir(anahtar):
    return hafiza.get(anahtar)
