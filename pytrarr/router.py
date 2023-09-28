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
    
    
    # return {
    #     'search': search, 
    #     'status': 200,
    #     'result': [
    #         {
    #             'title': 'Title 1',
    #             'subtitle': 'Subtitle 1'
    #         },
    #         {
    #             'title': 'Title 2',
    #             'subtitle': 'Subtitle 2'
                
    #         },
    #         {
    #             'title': 'Title 3',
    #             'subtitle': 'Subtitle 3'
    #         },
    #         {
    #             'title': 'Title 4',
    #             'subtitle': 'Subtitle 4'
    #         },
    #         {
    #             'title': 'Title 5',
    #             'subtitle': 'Subtitle 5'
    #         }
    #     ]
    # }

@app.get('/api/content/genres/{locale}', status_code=200)
async def genres(locale: str):
    async with AsyncClient() as client:
        response = await client.get(f'https://api.justwatch.com/content/genres/locale/{locale}')
        response.raise_for_status()
        return response.json()