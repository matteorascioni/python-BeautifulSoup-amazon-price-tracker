# Before to run this program, run this commands
# python -m venv
# pip3 install requests
# pip3 install lxml
# pip3 install bs4
import requests
import lxml
from bs4 import BeautifulSoup

MY_EMAIL = "" #Put your email here
MY_PASSWORD = "" #Put your AppPassword (take a look in google account -> Security --> App Password)
YOUR_SMTP_ADDRESS = "smtp.gmail.com" # <- example
BUY_PRICE = 0 #Set your buy_price here to recive the email

url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

if price_as_float < BUY_PRICE:
    # Send an email to the user
    message = f"{title} is now {price}"
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='', #Email addresses to contact
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )