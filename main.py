import os

import requests

from scrape.scrape import Scrape
from whatsapp_api.whatsapp import Whatsapp


def main():
    scrape = Scrape()
    whatsapp = Whatsapp(scrape.scrape())
    response = whatsapp.send_message()
    print(response)


if __name__ == "__main__":
    main()
