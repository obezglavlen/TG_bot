from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def back_button():
    return InlineKeyboardButton(text="⬅ Назад", callback_data="cb_anime_back")


def categories_menu_keyboard():
    buttons = [
        {
            "name": "Переглянуті",
            "cb": "seen"
        },
        {
            "name": "Покинуті",
            "cb": "abandoned"
        },
        {
            "name": "Улюбені",
            "cb": "liked"
        },
        {
            "name": "Дивлюся",
            "cb": "watching"
        }
    ]

    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 2
    keyboard.add(
        *[
            InlineKeyboardButton(
                text=category["name"], callback_data=f"cb_anime_category_{category['cb']}"
            )
            for category in buttons
        ]
    )
    keyboard.add(back_button())

    return keyboard


def main_menu_keyboard():
    buttons = [
        {
            "name": "Додати аніме",
            "cb": "add"
        },
        {
            "name": "Видалити аніме",
            "cb": "remove"
        },
        {
            "name": "Подивитися списки",
            "cb": "categories"
        }
    ]

    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 1
    keyboard.add(
        *[
            InlineKeyboardButton(
                text=button["name"], callback_data=f"cb_anime_{button['cb']}"
            )
            for button in buttons
        ]
    )

    return keyboard


menus = {
    "main_menu": main_menu_keyboard(),
    "add_menu": categories_menu_keyboard(),
    "remove_menu": categories_menu_keyboard(),
    "show_menu": categories_menu_keyboard(),
}
