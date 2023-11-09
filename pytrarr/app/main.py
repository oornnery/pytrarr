"""
dasdas
"""
from nicegui import ui


class Section(ui.element):
    """UI Section"""
    def __init__(self, 
            column: bool = False,
            bg_color: str = 'bg-gray-100',
            border: bool = True,
            border_color: str = 'border-gray-300',
            width: str = 'w-full',
            height: str = '',
            padding: str = 'p-4',
            radius_size: str = 'rounded-lg',
            shadow: str = '',
            classes: str = '',
            props: str = ''
        ) -> None:
        super().__init__(tag='section')
        self.classes(f'{padding} {width} {height} {bg_color} {shadow} {classes}')
        self.props(props)
        if column:
            self.classes('flex flex-col')
        else:
            self.classes('flex flex-row')
        if border:
            self.classes(f'border {border_color}')
        if radius_size:
            self.classes('rounded-lg')

@ui.page('/')
def main_app() -> None:
    """main app - Home Page"""
    def input_callback(input_var: str) -> None:
        ui.notify(f'Searching for {input_var}')

    # Based on the template
    with ui.column().classes('w-full h-screen'):
        with Section(shadow='shadow-lg', column=True, classes='h-screen w-full'):
            ui.label('Search torrent').classes('text-3xl font-mono-semibold my-1')
            with ui.input(label='Search', placeholder='Search...') as input_var:
                input_var.props('outlined')
                input_var.classes('my-1')
                ui.icon('search').classes('text-black m-auto text-2xl cursor-pointer')\
                    .on('click', lambda: input_callback(input_var.value))
                input_var.on('keydown.enter', lambda: input_callback(input_var.value))
            with ui.expansion(icon='filter_list').classes('my-1'), ui.column()\
                .classes('w-full px-4 py-2'):
                ui.label('Advanced filter').classes('text-sm font-mono-semibold text-gray-400')
                with Section(padding='p-0', border=False, classes='w-full justify-between'):
                    options = {
                        f'{i}': {
                            'options': [
                                'All','Option 1','Option 2','Option 3','Option 4','Option 5'
                                ],
                            'label': f'Option {i}',
                            'value': 'All',
                            'multiple': True,
                            'with_input': True,
                        } for i in range(1, 6)
                    }
                    for option_value in options.values():
                        ui.select(**option_value).classes('mx-2')
            with Section(padding='p-0') as section_content:
                # section_content.visible = False
                ui.label('Content').classes('text-3xl font-mono-semibold my-1')


if __name__ in {"__main__", "__mp_main__"}:
    ui.run()
