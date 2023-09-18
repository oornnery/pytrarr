from nicegui import ui
from nicegui.events import KeyEventArguments
from httpx import AsyncClient
from templates import (
    add_result_item
)

# from router import (
#     search,
# )

from pytrarr.api import api


URL_BASE = "http://localhost:8080/api/"

async def search_submit(slot: ui.grid, input: ui.input):
    if input.value == '':
        return ui.notify("Error: Input cannot be empty", position='top-right', color='red')
    
    async with AsyncClient() as client:
        search = await client.get(URL_BASE + 'search/' + input.value)
    
    if search.status_code != 200:
        return ui.notify("Error: " + str(search.status_code), position='top-right', color='red')
    slot.visible = True
    slot.clear()
    with slot:
        for x in search.json():
            add_result_item(x)
    input.set_value("")    



dark = ui.dark_mode(value=True, on_change=lambda: dark.enable)
    
@ui.page('/')
@ui.page('/home')
def page_home():
    # header
    with ui.header(elevated=True).classes('items-center'):
            # ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
            with ui.row().classes('justify-between'):
                ui.link('PYTRARR', target="home").classes('text-white text-lg no-underline hover:underline font-bold cursor-pointer')
            ui.switch(on_change=lambda: dark.enable).classes('cursor-pointer')
    # Left Menu            
    # with ui.left_drawer(fixed=False, elevated=True, bordered=True) as left_drawer:
    #     ui.label('MENU')
    
    #
    # Content
    #
    # input
    with ui.row().classes('flex flex-col items-center w-full h-full mx-4'):
        
        with ui.row().classes('flex flex-col w-full w-max-24 m-auto'):
            input = ui.input('Search', placeholder='Search').classes('w-96')
            ui.button('Search', on_click=lambda: search_submit(search_content, input)).classes('')
            
        with ui.grid(columns=4).classes('w-full h-100 rounded-md bg-gray-100') as search_content:
            search_content.visible = False




    with ui.footer():
        ui.label('FOOTER')
        


ui.run()
