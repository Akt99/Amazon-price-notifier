<div align="center">

# 🛒 Amazon Price Notifier 📩  
### *Track Amazon product prices & get notified instantly when price drops!*

<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2ZyYWZlMWI0cGU2aWZzM2RkZjJ3OHZ5YWRpYWpuNmVheTBhZnF2dCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7aCTfyhYawdOXcFW/giphy.gif" width="300" />

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-bs4-4CAF50?style=for-the-badge)
![Requests](https://img.shields.io/badge/Requests-HTTP-000000?style=for-the-badge&logo=python&logoColor=white)
![SMTP](https://img.shields.io/badge/SMTP-Email%20Alert-EA4335?style=for-the-badge&logo=gmail&logoColor=white)
![Amazon](https://img.shields.io/badge/Amazon-Live%20Tracking-FF9900?style=for-the-badge&logo=amazon&logoColor=black)

</div>

---

## ✨ What is Amazon Price Notifier?

**Amazon Price Notifier** is a Python automation project that scrapes the **live product title and price** from Amazon and sends an **email notification** whenever the product price goes **below your desired target price**.

✅ Scrapes Amazon product price in real time  
✅ Extracts product title automatically  
✅ Alerts user via Gmail SMTP  
✅ Uses `.env` to keep credentials safe  
✅ Works with real Amazon product pages (with headers)

---

## ⚙️ How it Works (Workflow)

```txt
Amazon Product Link
        |
        v
Request Page (headers)
        |
        v
Parse HTML using BeautifulSoup
        |
        v
Extract Title + Price
        |
        v
Convert price → float
        |
        v
Compare with BUY_PRICE
   |             |
   | (low)       | (high)
   v             v
Send Email ✅   Print Status ❌
