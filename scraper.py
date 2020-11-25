import requests
from bs4 import BeautifulSoup

#Getting the url of the product verifying it and making it shorter.
def extract_url(url):
    if(url.find("www.amazon.in")!= -1):
        index = url.find("/dp/")
        #print(index)
        if index!=-1 :
            index2 = index+14
            url = "https://www.amazon.in&quot" + url[index:index2]
        else:
            index =url.find("/gp/")
            #print(index)
            if(index!=-1):
                index2 = index + 22
                url = "https://www.amazon.in&quot" + url[index:index2]

            else:
                url =None
    else:
        url = None
    return url

def convert_price(price):
    converted_price = price.replace(",","")
    converted_price = converted_price.replace("₹","")
    converted_price = converted_price.replace(" ","")
    converted_price=float(converted_price)

    return converted_price

def get_product_details(url):
    headers ={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0"}
    details = {"name":"", "price":0, "deal":True, "url":""}
    _url = extract_url(url)
    if _url is None:
        details = None

    else:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        title = soup.find(id="productTitle")
        if soup.find(id="priceblock_dealprice") is not None:
            price = soup.find(id="priceblock_dealprice")
        else:
            details["deal"] = False
            price = soup.find(id="priceblock_ourprice")

        if title is not None and price is not None:
            details["name"] = title.get_text().strip()
            details["price"] = convert_price(price.get_text())
            details["url"] = _url

        else:
            details = None

    return details

value= input("Insert the Product URL(Amazon): ")
print(get_product_details(value))
"""
Other Data:
Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0
productTitle
priceblock_ourprice
priceblock_dealprice
"""