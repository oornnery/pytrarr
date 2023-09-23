import profile
from nicegui import app
from justwatch import JustWatch

from rich.console import Console

console = Console()

@app.get('/api/search/{search}', status_code=200)
def search(search: str):
    just_watch = JustWatch(country='BR')
    if search:
        return just_watch.search_for_item(search)
    
    return {
        'search': search, 
        'status': 200,
        'result': [
            {
                'title': 'Title 1',
                'subtitle': 'Subtitle 1'
            },
            {
                'title': 'Title 2',
                'subtitle': 'Subtitle 2'
                
            },
            {
                'title': 'Title 3',
                'subtitle': 'Subtitle 3'
            },
            {
                'title': 'Title 4',
                'subtitle': 'Subtitle 4'
            },
            {
                'title': 'Title 5',
                'subtitle': 'Subtitle 5'
            }
        ]
    }
