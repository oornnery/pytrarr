from typing import Any
from rich.console import Console

site_base = [
    'https://solidtorrents.to/torrents/rick-and-morty-vs-genocider-2020-1080p-dual-lat-b7182/6500ba0e5f0837d369a3730a/',
    'https://solidtorrents.to/library/stranger-things-a30b3/6050f4750ab2df3768993cb1',
]
torrent_urls = [
    'https://torrentflix.net/', # Robot
    'https://megatorrents.com.br/', # Robot
    'https://megadostorrents.info/' # Robot
    'https://filmeshdtorrent.megatorrents.info/', # Robot
    'https://nerdfilmes.com.br/', # Link
    'https://gratistorrent.com/', # Link
    'https://capitaofilmes.com/', # Robot
    'https://nickfilmes.net/', # Link
    'https://emtorrents.com/', # Link
    'https://www.tronodotorrent.com/'
    'https://sapotorrent.com/', # Link
    'https://flixtorrentx.org/' # Robot
    'https://1337x.to/home/',
    # Anime
    'https://www.skyanimeshd.site/',
    'https://darkmahou.org/',
    'https://seriesmp4.tv/',
    'https://www.animestotais.xyz/',
    'https://www.magnetdl.com/',
    'https://pirateproxy.live/'
    
]

torrent_novela = [
    'https://gratistorrent.com/avenida-brasil-completa-download-torrent/',
    'https://archive.org/details/avenida.-brasil.-103.-hdtv.-xvi-d.x-264.-novelas-hdtv.-23.07.12.-seg-feira_202107',
    'https://wdfdownload.blogspot.com/p/vai-na-fe.html',
    
]

database_catalog = [
    'https://www.justwatch.com/br/filme/oppenheimer',
    'https://images.justwatch.com/poster/306877943/s276/',
    'https://images.justwatch.com/poster/306877943/s166',
    'https://www.imdb.com/title/tt4574334/'
    
]


console = Console()
payload = {}
# API JustWatch

from httpx import AsyncClient
from pytrarr.utils.dataclass import (
    # API JustWatch
    Locales,
    LocalesInfo,
    
    # API Content
    MediaContent, 
    Genres,
)

class OMDBAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://www.omdbapi.com/"
        self.headers = {
            "Accept-Language":"pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6"
        }
        self.client = AsyncClient(
            base_url=self.base_url,
            params={"apikey": "697a47e2"},
            headers=self.headers,
        )

    async def search(self, 
            search: str,
            type: str="",
            year: str="", 
            page: int=1, 
            data_type: str = "json",
        ):
        """API OMDB http://www.omdbapi.com/

        Args:
            search (str): Movie title to search for.
            type (str, optional): Type of result to return. Defaults to <empty>.
            year (str, optional): Year of release. Defaults to <empty>.
            page (int, optional): Page number to return. Defaults to 1.
            data_type (str, optional): The data type to return. Defaults to "json".
        Returns:
            dict: Content 
        """
        params = {
            "s": search
        }
        # https://www.imdb.com/find/?q=vai%20na%20fe&s=tt&exact=true
        # https://cinemagoer.readthedocs.io/en/latest/usage/quickstart.html
        response = await self.client.get(self.base_url, params=params, headers=self.headers)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Request failed"}

if '__main__' == __name__:
    import asyncio
    async def tests():
        jw = OMDBAPI(api_key="")
        
        console.print(await jw.search("vai na fe"))

    asyncio.run(tests())
    