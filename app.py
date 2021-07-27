from fastapi import FastAPI
from scraper import Scraper


app = FastAPI()
quotes = Scraper()


@app.get("/v1/quotes/{cat}")
async def read_item(cat):
    return quotes.scrapequotes(cat)

@app.get("/v1/ecommerce/{cat}")
async def read_product(cat):
    return quotes.scrapeecommerce(cat)