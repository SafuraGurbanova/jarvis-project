import commands

print("Hoş geldin! Mini Jarvis aktif. 'cik' yazarak kapatabilirsin.")
while True:
    komut = input(">> ").lower().strip()

    if komut == "cik":
        print("Görüşürüz.")
        break

    commands.cevapla(komut)
