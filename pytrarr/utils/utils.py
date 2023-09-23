from justwatch import JustWatch
from httpx import AsyncClient
from dataclass import MediaContent, Gender, Genres
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
jw = JustWatch()


def search_just_api(search: str, country: str = 'BR') -> MediaContent:
    
    
    
    return MediaContent(
        
    )

content_type: str


def jw_get_genres(country: str = 'BR') -> Genres:
    global jw
    jw.country=country
     
    return Genres(
        [
            Gender(**gender) for gender in jw.get_genres()
        ]
    )

def jw_get_providers(country: str = 'BR'):
    global jw
    jw.country=country
    
    return jw.get_providers()

def jw_search_id(country: str = 'BR', id: int = 1):
    global jw
    jw.country=country
    
    return jw.get_title(id)

def jw_search_title(country: str = 'BR', id: int = 1):
    global jw
    jw.country=country
    
    return jw.get_title(id)

def jw_get_season(country: str = 'BR', id: int = 1):
    global jw
    jw.country=country
    
    return jw.get_title(id)

def jw_title_id(country: str = 'BR', id: int = 1):
    global jw
    jw.country=country
    
    return jw.get_title(id)


console.print(jw_providers()[0])