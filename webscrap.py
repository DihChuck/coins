from typing import Any, Iterable
from zenrows import ZenRowsClient
from scrapy.http import Response
from parsel import Selector
import scrapy, cloudscraper, json


scraper = cloudscraper.create_scraper() 

def latestPlayers():

    r = scraper.get('https://www.futwiz.com/en/fc24/players/latest')
    response = Selector(text = r.text)
    resp = response.xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[1]/a[1]').get()


    for p in resp.xpath(".//p"):  # extracts all <p> inside
        print(p.get())
        #href_xpath = link.xpath("@href").get()
        #img_xpath = link.xpath("img/@src").get()
        #print(f"Link number {index} points to url {href_xpath!r} and image {img_xpath!r}")

latestPlayers()