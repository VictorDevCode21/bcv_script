import os

# import certifi
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


class Scrape:

    def __init__(self):
        self

    def scrape(self):
        load_dotenv()
        url = os.getenv("url")
        response = requests.get(url, verify=False)

        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")

            price = soup.find("div", id="dolar").find("strong").get_text()
            if price is not None:
                # print(price)
                return price
            if price is None:
                print("Error")
        else:
            print("Error")

        return price
