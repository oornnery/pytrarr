from nicegui import app
from httpx import AsyncClient

from rich.console import Console
from imdb import Cinemagoer, IMDbError, Movie

console = Console()
imdb = Cinemagoer()

@app.get('/api/search/', status_code=200)
def search(s: str):
    
    try:
        query = imdb.search_movie(s)
        console.log(f'SearchSuccess: {s}')
        console.log([q.movieID for q in query])
        return {
            'search': s,
            'status': 200,
            'error': None,
            'result': [q.update({'movieID': q.movieID}) for q in query]
        }
    except IMDbError as e:
        console.log(f'SearchError: {e} - {s}')
        return {
            'search': s,
            'status': 500,
            'error': e,
            'result': []
        }

@app.get('/api/torrents', status_code=200)
def search_torrent(name: str = '', moveId: str = '', years: str = '', temp: str = '', page: str = ''):
    ...
    


@app.get('/api/content/genres/{locale}', status_code=200)
async def genres(locale: str):
    async with AsyncClient() as client:
        response = await client.get(f'https://api.justwatch.com/content/genres/locale/{locale}')
        response.raise_for_status()
        return response.json()