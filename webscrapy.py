import scrapy
import json
import warnings
from connection import insertPlayers

class fifaData(scrapy.Spider):
    name = 'coins'

    custom_settings = {
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        
    }

    warnings.filterwarnings("ignore", category=scrapy.exceptions.ScrapyDeprecationWarning)

    start_urls = [
        'https://www.futwiz.com/en/fc24/players/latest'
    ]

    def parse(self, response, **kwargs):
        
        campos = "link, rating, name, position, img"

        for quote in response.css("div a.player-card"):

            yield {
                "link": quote.css("a::attr(href)").get(),
                "rating": quote.css("div.card-24-pack-rating::text").get(),
                "name": quote.css("div.card-24-pack-name::text").get(),
                "position": quote.css("div.card-24-pack-position::text").get(),
                "img": quote.css("div.card-24-pack-face-alt img::attr(src)").get(),
            }

            valores = [
                 quote.css("a::attr(href)").get(),
                 quote.css("div.card-24-pack-rating::text").get(),
                 quote.css("div.card-24-pack-name::text").get(),
                 quote.css("div.card-24-pack-position::text").get(),
                 quote.css("div.card-24-pack-face-alt img::attr(src)").get()
            ]

            insertPlayers(campos,valores)

