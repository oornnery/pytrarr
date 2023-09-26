from nicegui import ui
from nicegui.events import KeyEventArguments
from httpx import AsyncClient
from templates import (
    add_result_item
)

from pytrarr.utils.utils import (
    JustWatch
)

# from router import (
#     search,
# )

import pytrarr.router


jw = JustWatch('BR')

URL_BASE = "http://localhost:8080/api"

async def search_submit(slot: ui.grid, input: ui.input):
    if input.value == '':
        return ui.notify("Error: Input cannot be empty", position='top-right', color='red')
    
    async with AsyncClient() as client:
        search = await client.get(URL_BASE + 'search/' + input.value)
    
    if search.status_code != 200:
        return ui.notify(f"Error: {search.status_code}", position='top-right', color='red')
    slot.visible = True
    slot.clear()
    with slot:
        for x in search.json():
            add_result_item(x)
    input.set_value("")    



dark = ui.dark_mode(value=True)
    
@ui.page('/')
@ui.page('/home')
async def page_home():
    ##############
    ### Header ###
    ##############
    #TODO: Add dark mode
    #TODO: Add Nav Pages
    await jw.set_locale()
    
    with ui.header(add_scroll_padding=True).classes('items-center'):
            # ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
            with ui.row().classes('justify-between'):
                ui.link('PYTRARR', target="home").classes('text-white text-lg no-underline hover:underline font-bold cursor-pointer')
            ui.switch(on_change=lambda: dark.enable).classes('cursor-pointer')
    
    ############
    ### Body ###
    ############
    
    # TODO: Add Title
    # TODO: Add search
    # TODO: Add Filters
    # TODO: Add Section result
    # TODO: Add Cards
    # TODO: Add List
    # TODO: Add Footer
    
    with ui.row().classes(
        'bg-gray-100 p-4 w-full h-full flex flex-col items-center justify-center'
        ) as main:
        
        ### TITLE ###
        with ui.row():
            ui.label('Media Search').classes(
                'text-4xl font-mono-semibold'
            )

        ### INPUT ###
        with ui.row().classes('m-3') as search:
            with ui.row().classes(
                'relative mb-4 flex w-full flex-wrap items-stretch'
            ):
                input = ui.input('Search', placeholder='Search').classes(
                    'relative m-0 w-96 min-w-0 block flex-auto rounded-l \
                    border border-solid border-neutral-300 \
                    bg-transparent bg-clip-padding px-3 py-[0.25rem] \
                    text-base font-normal leading-[1.6] text-neutral-700 \
                    outline-none transition duration-200 ease-in-out focus:z-[3] \
                    focus:border-primary focus:text-neutral-700 \
                    focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] \
                    focus:outline-none dark:border-neutral-600 dark:text-neutral-200 \
                    dark:placeholder:text-neutral-200 dark:focus:border-primary'
                )
                ui.button(icon='search',on_click=lambda: search_submit(search_content, input)).classes(
                    'relative z-[2] flex items-center rounded-r bg-primary px-6 py-2.5 text-xs font-medium uppercase leading-tight text-white shadow-md transition duration-150 ease-in-out hover:bg-primary-700 hover:shadow-lg focus:bg-primary-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-primary-800 active:shadow-lg'
                )

            with ui.row().classes('w-full flex-1') as filters:
                genres = await jw.get_genres()
                ui.select(
                    options=[gen.translation for gen in genres],
                    label='Category', 
                    with_input=True, 
                    multiple=True, 
                    clearable=True,
                    on_change=lambda e: print(e.value)
                ).classes(
                    'w-36 h-4'
                )
        with ui.grid(columns=4).classes('w-full h-100 rounded-md bg-gray-100') as search_content:
            search_content.visible = True




    with ui.footer():
        ui.label('FOOTER')
        


ui.run()
