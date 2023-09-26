from nicegui import ui


def add_result_item(info: dict):
    url = "https://images.justwatch.com"
    poster = info['poster'][:-9]
    profile = "s276"
    print(url+poster+profile)
    
    with ui.grid(rows=1).classes('bg-gray-200 rounded-lg p-4'):
        ui.image(url+poster+profile).classes('w-100 h-100')
        ui.label(str(info['title'])).classes('sm:text-1 xl:text-3')
        ui.label(str(info['id'])).classes('')