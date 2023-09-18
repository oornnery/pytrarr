

import select
from httpx import AsyncClient
from parsel import Selector
from pytrarr.scrappers.utils import getSource

from rich.console import Console

console = Console()

from dataclasses import dataclass, field

@dataclass
class SearchTorrent:
    title: str
    original_title: str  = field(default_factory=str)
    year: str = field(default_factory=str)
    genres: list[str] = field(default_factory=list)
    language: list[str] = field(default_factory=list)
    subtitles: list[str] = field(default_factory=list)
    video_format: str = field(default_factory=str)
    quality: str = field(default_factory=str)
    video_size: str = field(default_factory=str)
    audio_quality: str = field(default_factory=str)
    video_quality: str = field(default_factory=str)
    duration: str = field(default_factory=str)
    banner: str = field(default_factory=str)
    url_site: str = field(default_factory=str)
    url_torrent: str = field(default_factory=str)



async def searchTorrentFlix(
        query: str = "", 
        page: int = 1
    ):

    def get_urls_in_page(
            content: str, 
            selector: str, 
            selector_title: str,
            selector_url: str, 
        ):
        
        sel = Selector(text=content)
        elements = sel.css(selector)
        for element in elements:
            title = element.css(selector_title).get("")
            url = element.css(selector_url).get("")
            # console.log(f'Title: {title} | URL: {url}')
            yield SearchTorrent(title=title, url_torrent=url)

    def get_information_in_page(
            search_torrent: SearchTorrent, 
            content: str,
            selector: str,
            selector_torrent: str, 
            selector_information: str,
        ) -> SearchTorrent:
        
        sel = Selector(text=content)
        element = sel.css(selector)
        url_torrent = element.css(selector_torrent).get("")
        information = [el.split(':') for el in element.css(selector_information).getall() if ':' in el]
        # console.log(information)
        
        search_torrent.language = [information[1][1]]
        search_torrent.subtitles = [information[2][1]]
        search_torrent.video_format = information[3][1]
        search_torrent.quality = information[4][1]
        search_torrent.video_size = information[5][1]
        search_torrent.duration = information[7][1]
        search_torrent.audio_quality = information[8][1]
        search_torrent.video_quality = information[9][1]
        search_torrent.url_torrent = url_torrent
        
        return search_torrent

    async with AsyncClient(follow_redirects=True) as client:
        selector_url = "#main > div > div.movies-list > div"
        selector_url_title = 'div.title > a::text'
        selector_url_url = 'a::attr(href)'
        
        selector_information = "#main > div > div.post-block > div.col-left > div.info"
        selector_information_torrent = 'a.torrent::attr(href)'
        selector_information_info = 'ul li::text'

        result = []
        console.log("Getting pages: https://torrentflix.net/page/'")
        while True:
            #
            search = await client.get('https://torrentflix.net/page/' + str(page))
            if search.status_code == 404:
                break
            #
            console.log("page: " + str(page)+ " Status: " + str(search.status_code))
            page += 1
            for url in get_urls_in_page(
                    search.text,
                    selector_url,
                    selector_url_title,
                    selector_url_url
                ):
                search2 = await client.get(url.url_torrent)
                result.append(
                    get_information_in_page(
                        url, 
                        search2.text, 
                        selector_information, 
                        selector_information_torrent, 
                        selector_information_info
                    )
                )
        console.print(result)
        console.print(len(result))



async def searchMegatorrent(query="", page=1):
    async with AsyncClient() as client:
        result = []
        if query:
            search = await client.get('https://torrentflix.net/', params={'s': query})
            if search.status_code == 404:
                return result
            result.append(search.content)
        else:
            while True:
                search = await client.get('https://megatorrents.com.br/baixar-filmes-utorrent/page/' + str(page))
                if search.status_code == 404:
                    console.print('Total de páginas: ' + str(page))
                    break
                
                page += 1

if __name__ == "__main__":
    import asyncio
    asyncio.run(searchTorrentFlix())