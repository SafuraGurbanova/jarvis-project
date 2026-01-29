#  Jarvis – Türkçe Terminal Yapay Zekâ Asistanı

Jarvis, Python ile geliştirilmiş, Türkçe konuşabilen bir terminal tabanlı yapay zekâ asistanıdır.

Bu proje; kullanıcının ruh halini analiz eden, problemleri adım adım keşfeden ve çözüm önerileri sunan bir konuşma sistemi oluşturmayı hedefler.

Proje öğrenme ve gelişim amaçlıdır ve aktif olarak geliştirilmektedir.

---

##  Özellikler

- Türkçe komut algılama  
- Duygu durumu tespiti (pozitif / negatif)  
- Problem takibi (okul, sınav, aile vb.)  
- Hafıza sistemi (custom memory)  
- Sebep analizi (`neden böyleyim`)  
- Dinamik çözüm önerileri  
- State sistemi ile konuşma akışı yönetimi  

---

##  Kullanılan Teknolojiler

- Python  
- Basit NLP (kelime eşleştirme tabanlı)  
- State Machine mantığı  
- Özel memory sistemi  

---

##  Çalıştırma

```bash
python core.py

##  Proje Yapısı

jarvis-project/
│
├── core.py        # Ana program
├── commands.py    # Konuşma mantığı
├── memory.py      # Hafıza sistemi

##  Nasıl Çalışır?

1. Kullanıcı girdisi normalize edilir

2. Intent algılanır

3. State kontrol edilir

4. Problem tespit edilir

5. Alt problemler sorgulanır

6. Ağırlık hesaplanır

7. neden böyleyim ile çözüm üretilir

## Gelecek Hedefleri

OpenAI entegrasyonu

Sesli giriş / çıkış

GUI arayüz

Daha gelişmiş NLP

Kalıcı veritabanı sistemi

## Geliştiriciler

Levent Efe Çiftçi

Safura Gurbanova

Bu proje iki öğrenci geliştirici tarafından yürütülmektedir.
Odak alanları: Yapay zekâ sistemleri ve backend geliştirme.

## Not

Bu proje eğitim amaçlıdır ve sürekli geliştirilmektedir.