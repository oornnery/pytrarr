from nicegui import ui
from nicegui.events import KeyEventArguments


from modules import TMDB
from templates import (
    add_result_item
)



URL_BASE = "http://localhost:8080/api"

async def search_submit(slot: ui.grid, query: str):
    if query == '':
        return ui.notify("Error: Input cannot be empty", position='top-right', color='red')
    
    db = TMDB()
    
    r = await db.search(query)
    
    slot.visible = True
    slot.clear()
    
    with slot:
        for x in r.get('results', {}):
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
    #TODO: Add Nav Page
    
    with ui.header(add_scroll_padding=True).classes('items-center'):
            # ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
            with ui.row().classes('justify-between'):
                ui.link('PYTRARR', target="home").classes('text-white text-lg no-underline hover:underline font-bold cursor-pointer')
            ui.switch(on_change=lambda: dark.enable).classes('cursor-pointer')
    
    ############
    ### Body ###
    ############
    
    
    with ui.column().classes(
        'bg-gray-100 p-4 w-full h-full items-center justify-center'
        ) as main:
        
        ### TITLE ###
        with ui.row() as title:
            ui.label('Media Search').classes(
                'text-4xl font-mono-semibold'
            )

        ### INPUT ###
        with ui.column().classes('items-center justify-center') as search:
            with ui.row().classes(
                'mb-4'
            ):
                input = ui.input('Search', placeholder='Search').classes(
                    'w-96'
                ).on(
                    'keydown.enter', lambda: search_submit(search_content, input.value)
                )
                ui.button(icon='search',on_click=lambda: search_submit(search_content, input.value)).classes(
                    'w-20 my-4'
                )

            with ui.row().classes() as filters:
                genres = []
                for _ in range(0,3):
                    with ui.column().classes('items-left justify-center'):
                        ui.label('Category').classes('m-0 p-0 text-end text-gray-')
                        ui.select(
                            options=[
                                'All', 
                                'Action', 
                                'Adventure', 
                                'Animation', 
                                'Comedy', 
                                'Crime', 
                                'Drama', 
                                'Fantasy', 
                                'Horror', 
                                'Mystery', 
                                'Romance', 
                                'Sci-Fi', 
                                'Thriller', 
                                'War', 
                                'Western'
                            ],
                            with_input=False, 
                            multiple=True, 
                            clearable=True,
                            on_change=lambda e: print(e.value)
                        ).classes(
                            'w-40 h-10 truncate pl-1 text-center text-gray-500 border border-gray-300 rounded-md'
                        )
        search_content = ui.grid(columns=4).classes('w-full h-100 rounded-md bg-gray-100')
        with search_content:
            search_content.visible = True




    with ui.footer():
        ui.label('FOOTER')
        


ui.run()
