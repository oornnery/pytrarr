from attr import dataclass
from nicegui import ui

def search_submit(input: ui.input):
    print(input.value)
    input.set_value("")    


def add_result_item(info: dict):
    with ui.grid(rows=1).classes('bg-gray-200 rounded-lg p-4'):
        ui.image("https://dummyimage.com/420x260").classes('w-full max-w-sm mx-auto')
        ui.label("Title").classes('sm:text-1 xl:text-3')
        ui.label("Subtitle").classes('')
    
    
    
@ui.page('/home')
def page_home():

    # header
    with ui.header(elevated=True).classes('items-center'):
            ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
            with ui.row().classes('justify-between'):
                ui.label('PYTRARR')
    # Left Menu            
    with ui.left_drawer(fixed=False, elevated=True, bordered=True) as left_drawer:
        ui.label('MENU')
    
    #
    # Content
    #
    # input
    ui.label('Search:')
    with ui.row():
        input = ui.input()
        ui.button('Search', on_click=lambda: search_submit(input))
    with ui.grid(columns=4).style('background-color: #3874c8').classes('p-4 w-full'):
        for x in range(5):
            
            add_result_item({'title': 'Title', 'subtitle': 'Subtitle'})
        



    with ui.footer():
        ui.label('FOOTER')


ui.run()