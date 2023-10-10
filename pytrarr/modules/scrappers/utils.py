from pydoc import cli
from httpx import AsyncClient
from cloudscraper import create_scraper


scrapper = create_scraper()



def getSource(url):
    source = scrapper.get(url, timeout=5)
    source.raise_for_status()
    return source.text

async def get(url):
    async with AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response

