from nicegui import ui


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