import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


smt = soup.find("div", attrs={"class":"info_place clear type_longtit4"}).find_all("dl")

for row in smt:
    if row.find("dt") and row.find("dd"):
        print(row.find("dt").get_text()+":"+row.find("dd").get_text())
    elif row.find("dt") and row.a["href"]:
        print(row.find("dt").get_text() + ":"+ row.find_all("a", attrs={"class":"f_link"}))

