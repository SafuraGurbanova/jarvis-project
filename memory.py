import json
import os

FILE = "memory.json"

def oku():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def yaz(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def kaydet(key, value):
    data = oku()
    data[key] = value
    yaz(data)

def getir(key):
    data = oku()
    return data.get(key)

# ilk mood
if getir("mood") is None:
    kaydet("mood", "normal")
