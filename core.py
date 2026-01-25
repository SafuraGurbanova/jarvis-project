import commands
import memory

isim = memory.getir("isim")

if isim:
    print(f"Hoş geldin {isim}, bende seni bekliyordum")
else:
    print("Hoş geldin, ben Jarvis. İsmini söyle tanışalım.")

while True:
    komut = input(">> ")

    if komut == "cik":
        print("Görüşürüz, çok özletme kendini.")
        break

    commands.cevapla(komut)
