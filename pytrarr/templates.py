from typing import Any

from nicegui import ui


theme = {
    'lightThemeColors': {
        'bg': 'bg-white',
        'fg': 'text-gray-800',
        'text': 'text-gray-700',
        'border': 'border-gray-300',
        'hover': 'hover:bg-gray-100',
        'focus': 'focus:bg-gray-100',
        'active': 'active:bg-gray-200'
        },
    'darkThemeColors': {
        'bg': 'bg-gray-900',
        'fg': 'text-white',
        'text': 'text-gray-400',
        'border': 'border-gray-700',
        'hover': 'hover:bg-gray-800',
        'focus': 'focus:bg-gray-800',
        'active': 'active:bg-gray-700'
        }
    }

# light_theme_colors = {
#     'primary': '#2196F3',
#     'secondary': '#FFC107',
#     'accent': '#9C27B0',
#     'dark': '#333333',
#     'light': '#FFFFFF',
#     'text': '#333333',
#     'secondary_text': '#666666',
#     'border': '#E0E0E0',
#     'hover': '#EEEEEE',
#     'focus': '#E0E0E0',
#     'active': '#CCCCCC'
# }

# dark_theme_colors = {
#     'primary': '#2196F3',
#     'secondary': '#FFC107',
#     'accent': '#9C27B0',
#     'dark': '#121212',
#     'light': '#333333',
#     'text': '#FFFFFF',
#     'secondary_text': '#CCCCCC',
#     'border': '#333333',
#     'hover': '#333333',
#     'focus': '#666666',
#     'active': '#888888'
# }

def add_result_item(info: dict):
    with ui.card().classes('p-4'):
        with ui.card_section().classes('h-full border-2 border-gray-200 border-opacity-60 rounded-lg overflow-hidden'):
            ui.image(
                info.get('full-size cover url', 'https://dummyimage.com/720x400')
            ).classes('lg:h-48 md:h-36 w-full object-cover object-center')
            with ui.row().classes('p-6'):
                # H2 Category
                ui.label(
                    f"{info.get('kind', 'N/A')} - {info.get('year', 'N/A')}"
                ).classes('tracking-widest text-xs title-font font-medium text-gray-400 mb-1')
                # H1 Title
                ui.label(
                    info.get('title', 'N/A')
                ).classes('title-font text-lg font-medium text-gray-900 mb-3')
                # P Description
                ui.label(
                    info.get('smart long imdb canonical title', 'N/A')
                ).classes('leading-relaxed mb-3')
            with ui.row().classes('flex items-center flex-wrap'):
                ui.link('Learn more').classes('text-indigo-500 inline-flex items-center md:mb-2 lg:mb-0')
                ui.icon('arrow right alt')
                

class Body(ui.column):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.classes('items-center justify-center w-full')
        self.props('')


class Card(ui.card):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.classes('')
        self.props('')

class Input(ui.input):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.classes('')
        self.props('outlined')
        self.call_back: Any = None
    
    def icon(self, 
        icon: str = 'search', 
        size: str = '12'
        ):
        with self:
            ui.icon(icon, size=size)\
                .classes(
                    'py-4 text-gray-400 text-2xl cursor-pointer'
                )\
                .on('click', self.callback)

    def callback(self, callback: Any):
        self.call_back = callback if self.call_back is None else self.call_back
        self.on('Enter', self.call_back(self.value))
class Header(ui.header):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.classes('')
        self.props('')


class Section(ui.row):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.classes('')
        self.props('')

class Title(ui.label):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.classes('text-3xl font-mono-bold')
        self.props('')

class SubTitle(ui.label):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.classes('text-2xl font-mono-semibold')
        self.props('')

class Filters(ui.expansion):
    pass

