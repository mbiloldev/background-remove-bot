# 🖼️ Background Remove Bot (Telegram)

Ushbu Telegram bot sun'iy intellekt (`rembg` kutubxonasi) yordamida rasmlarning orqa fonini (background) bir necha soniya ichida butunlay avtomatik ravishda olib tashlaydi. Bot hech qanday pullik API'larsiz, to'g'ridan-to'g'ri serverning o'zida rasmlarga ishlov beradi.

📌 **Bot manzili:** [@SizningBotizningUsernamei](https://t.me/bot_linki)

---

## ✨ Xususiyatlari (Features)

* ⚡ **Mutloq bepul va cheksiz:** Tashqi pullik API kalitlaridan foydalanmaydi (`rembg` orqali ishlaydi).
* 🎯 **Yuqori aniqlik:** Sun'iy intellekt modeli yordamida sochlar va murakkab qirralarni ham aniq ajratadi.
* 📁 **PNG Hujjat formatida yuborish:** Telegram rasmlarni siqib qo'ymasligi va shaffoflik (transparency) saqlanib qolishi uchun natijani `.png` hujjat (document) ko'rinishida qaytaradi.
* 🔄 **Asinxron arxitektura:** `aiogram 3.x` yordamida ko'plab so'rovlarni bir vaqtda tezkor qabul qiladi.

---

## 🛠️ Texnologiyalar (Built With)

* **Dasturlash tili:** Python 3.9+
* **Framework:** [aiogram 3.x](https://github.com/aiogram/aiogram) (Asinxron Telegram Bot kutubxonasi)
* **AI Model:** [rembg](https://github.com/danielgatis/rembg) (U2-Net modeliga asoslangan fonni o'chirish vositasi)
* **Rasm operatori:** [Pillow (PIL)](https://pillow.readthedocs.io/) (Rasmlar bilan ishlash uchun)

---

## 🚀 Ishga tushirish (Installation)

Botni o'zingizning kompyuteringiz yoki serveringizda ishga tushirish uchun quyidagi ketma-ketlikni bajaring:

### 1. Loyihani nusxalash (Clone)
```bash
git clone [https://github.com/mbiloldev/background-remove-bot.git](https://github.com/github_username/background-remove-bot.git)
cd background-remove-bot
