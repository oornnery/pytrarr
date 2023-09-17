from math import inf
from nicegui import ui


def add_result_item(info: dict):
    
    with ui.grid(rows=1).classes('bg-gray-200 rounded-lg p-4'):
        url = "https://images.justwatch.com"
        poster = info['poster'][:-9]
        profile = "s276"
        print(url+poster+profile)
        ui.image(url+poster+profile).classes('w-full max-w-sm mx-auto')
        ui.label(str(info['title'])).classes('sm:text-1 xl:text-3')
        ui.label(str(info['id'])).classes('')