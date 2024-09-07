from bs4 import BeautifulSoup
import requests as req
import smtplib
import os

from dotenv import load_dotenv

load_dotenv()
practice_url="https://appbrewery.github.io/instant_pot/"
live_url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = req.get(live_url,headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find(id="productTitle").get_text().strip()
    price_whole = soup.find(class_="a-price-whole")
    price_fraction = soup.find(class_="a-price-fraction")
    price_whole = price_whole.get_text().strip() if price_whole else "0"
    price_fraction = price_fraction.get_text().strip() if price_fraction else "00"

    if "." in price_whole:
        price=price_whole
    else:
        price=f"{price_whole}.{price_fraction}"

    try:
        price_as_float= float(price.replace(",",""))
        print(f"Price as float: {price_as_float}")
        print(f"Product Title :{title}")

        BUY_PRICE= 100.00
        if price_as_float< BUY_PRICE:
            message=f"{title} is on sale for ${price} !"
            print(message)

            with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), port =587) as connection:
                connection.starttls()
                connection.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
                connection.sendmail(
                        from_addr=os.getenv("EMAIL_ADDRESS"),
                        to_addrs="targetmail@gmail.com",
                        msg=f"Subject: Amazon Price Alert !\n\n {message}\n{live_url}".encode("utf-8")

                    )
        else:
            print(f"{title} is not below the target price. Current price: ${price_as_float}")
    except ValueError:
        print(f"Error parsing the price:{price}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
