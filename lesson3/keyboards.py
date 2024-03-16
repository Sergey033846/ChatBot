from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button1 = KeyboardButton(text='/start')
button2 = KeyboardButton(text='помощь')
button3 = KeyboardButton(text='узнай про Юпитер')
button4 = KeyboardButton(text='расскажи про биткойн')
button5 = KeyboardButton(text='найди про грибы')
button6 = KeyboardButton(text='что такое солнечное затмение')

keyboard1 = [
    [button1, button2, button3],
    [button4, button5, button6],
]

kb_wiki = ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)

# inline - клавиатуры

# меню категорий поиска
inline_button_search_category1 = InlineKeyboardButton(text='Континенты планеты Земля', callback_data='button_category_continents')
inline_button_search_category2 = InlineKeyboardButton(text='Планеты Солнечной системы', callback_data='button_category_planets')
inline_keyboard_search_categories_list = [
    [inline_button_search_category1],
    [inline_button_search_category2],
]
kb_inline_search_categories = InlineKeyboardMarkup(inline_keyboard=inline_keyboard_search_categories_list)

# кнопка возврата в главное меню
inline_button_menu_search_categories = InlineKeyboardButton(text='Вернуться к категориям', callback_data='button_menu_search_categories')

# меню "континенты"
inline_button_continent1 = InlineKeyboardButton(text='Африка', callback_data='button_continent_Африка')
inline_button_continent2 = InlineKeyboardButton(text='Австралия', callback_data='button_continent_Австралия')
inline_button_continent3 = InlineKeyboardButton(text='Евразия', callback_data='button_continent_Евразия')
inline_button_continent4 = InlineKeyboardButton(text='Антарктида', callback_data='button_continent_Антарктида')
inline_keyboard_search_continents_list = [
    [inline_button_continent1, inline_button_continent2],
    [inline_button_continent3, inline_button_continent4],
    [inline_button_menu_search_categories],
]
kb_inline_search_continents = InlineKeyboardMarkup(inline_keyboard=inline_keyboard_search_continents_list)

# меню "планеты"
inline_button_planet1 = InlineKeyboardButton(text='Меркурий', callback_data='button_planet_Меркурий')
inline_button_planet2 = InlineKeyboardButton(text='Венера', callback_data='button_planet_Венера')
inline_button_planet3 = InlineKeyboardButton(text='Земля', callback_data='button_planet_Земля')
inline_button_planet4 = InlineKeyboardButton(text='Марс', callback_data='button_planet_Марс')
inline_keyboard_search_planets_list = [
    [inline_button_planet1, inline_button_planet2],
    [inline_button_planet3, inline_button_planet4],
    [inline_button_menu_search_categories],
]
kb_inline_search_planets = InlineKeyboardMarkup(inline_keyboard=inline_keyboard_search_planets_list)