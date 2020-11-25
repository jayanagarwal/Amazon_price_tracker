import requests
from bs4 import BeautifulSoup

#Getting the url of the product verifying it and making it shorter.
def extract_url(url):
    if(url.find("www.amazon.in")!= -1):
        index = url.find("/dp/")
        if index!=-1 :
            index2 = index+14
            #Shortening The URL
            url = "https://www.amazon.in&quot" + url[index:index2]
        else:
            index =url.find("/gp/")
            #print(index)
            if(index!=-1):
                index2 = index + 22
                #Shortening the URL
                url = "https://www.amazon.in&quot" + url[index:index2]

            else:
                url =None
    else:
        url = None
    return url

def convert_price(price):
    #You can also use regex or any other way to convert the price.
    converted_price = price.replace(",","")
    converted_price = converted_price.replace("₹","")
    converted_price = converted_price.replace(" ","")
    converted_price=float(converted_price)

    return converted_price

def get_product_details(url):
    #1. Here the data inside header varies, google "My User Agent" and copy the result as the value in the headers key "User-Agent"
    headers ={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0"}
    details = {"name":"", "price":0, "deal":True, "url":""}
    _url = extract_url(url)
    if _url is None:
        details = None

    else:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        #The variables here such as productTitle , priceblock_ourprice and others are to be searched through the amazon website.
        #You can inspect the website and then find the id for the product name(productTitle), price(priceblock_ourprice/priceblock_dealprice)
        #When the item is on a deal we see "priceblock_dealprice" else we see "priceblock_ourprice" to check that we have used Deal in details.
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
