from bs4 import BeautifulSoup
import requests


def cryptoValue():
    url = 'https://coinmarketcap.com/ru/'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(response.text, "lxml")
    crypto = {}
    rows = soup.find("table", class_='cmc-table').find("tbody").find_all("tr")
    for i in range(10):
        crypto[rows[i].find_all("td")[2].find("p").text] = float(
            rows[i].find_all("td")[3].find("span").text[1:].replace(",", ""))
    return crypto


def currencyValue():
    url = 'https://cbr.ru/key-indicators/'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(response.text, "lxml")
    coin = {'RUB': float(1)}
    for i in range(1, 3):
        coin[soup.find_all("table")[1].find_all("tr")[i].find("div", class_="col-md-3 offset-md-1 _subinfo").text] = \
            float(soup.find_all("table")[1].find_all("tr")[i].find("td", class_="value td-w-4 _bold _end mono-num")
                  .text.replace(",", "."))
    return coin
