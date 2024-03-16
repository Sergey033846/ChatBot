import asyncio
import config
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import logging
import random
import wikipedia
from keyboards import kb_wiki, kb_inline_search_categories, kb_inline_search_planets, kb_inline_search_continents

# включаем логгирование
logging.basicConfig(level=logging.INFO)

router = Router()
router_planets = Router()
router_continents = Router()

class ChoiceSearchCategoriesAndElements(StatesGroup):
    choice_search_categories = State()
    choice_search_planets = State()
    choice_search_continents = State()

# создаем объект бота
bot = Bot(token=config.token)

# диспетчер
dp = Dispatcher()

dp.include_router(router)
dp.include_router(router_planets)
dp.include_router(router_continents)

# обработчик на команду start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    name = message.chat.ﬁrst_name
    command_list = "/start - запуск бота\n" \
                   "/info, /help - описание бота\n" \
                   "/search - поиск в Википедии"
    await message.answer(f"Привет, {name}!\nЯ твой первый бот в Telegram! 😊")
    await message.answer(f"Доступные команды:\n{command_list}")

# обработчик на команду search
# выбор категории поиска
@router.message(Command("search"))
async def cmd_search(message: types.Message, state: FSMContext):
    await message.answer("Давай поищем в Википедии!\nЧто будем искать?", reply_markup=kb_inline_search_categories)
    await state.set_state(ChoiceSearchCategoriesAndElements.choice_search_categories)

# возврат в меню выбора категорий поиска
@router.callback_query(F.data == "button_menu_search_categories")
async def cmd_search_categories(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Выберите категорию:", reply_markup=kb_inline_search_categories)
    await state.set_state(ChoiceSearchCategoriesAndElements.choice_search_categories)
    await callback.answer()

# выбор конкретной планеты, если выбрана категория "Планеты Солнечной системы"
@router.callback_query(F.data == "button_category_planets")
async def cmd_search_planets(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_search_category="Планета")
    await callback.message.answer("Выберите планету:", reply_markup=kb_inline_search_planets)
    await state.set_state(ChoiceSearchCategoriesAndElements.choice_search_planets)
    await callback.answer()

# обработчик на нажатие кнопки с названием планеты
@router.callback_query(ChoiceSearchCategoriesAndElements.choice_search_planets, F.data.startswith('button_planet_'))
async def print_search_planets(callback: types.CallbackQuery, state: FSMContext):
    planetCaption = callback.data.replace('button_planet_', '')

    user_data = await state.get_data()
    wiki_query = planetCaption + " " + user_data.get("chosen_search_category")

    await callback.message.answer(f'Твой запрос \"{wiki_query}\"')

    # обработка запроса в Википедию
    wikipedia.set_lang('ru')
    await callback.message.answer(f'Уже ищу в Википедии про {wiki_query}!\nПодожди чуть-чуть, пожалуйста.')
    wiki_results = wikipedia.search(wiki_query)
    if not wiki_results:
        await callback.message.answer('Ничего не найдено. Повторим?', reply_markup=kb_wiki)
    else:
        page_wiki = wikipedia.page(wiki_results[0])
        await callback.message.answer('Вот, что я нашел')
        await callback.message.answer(page_wiki.summary[:200])
        await callback.message.answer('Вот, где об этом указано')
        await callback.message.answer(page_wiki.url)

    await callback.message.answer("Продолжим поиск?", reply_markup=kb_inline_search_planets)

    await callback.answer()

# выбор конкретного континента, если выбрана категория "Континенты планеты Земля"
@router.callback_query(F.data == "button_category_continents")
async def cmd_search_continents(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_search_category="Континент")
    await callback.message.answer("Выберите континент:", reply_markup=kb_inline_search_continents)
    await state.set_state(ChoiceSearchCategoriesAndElements.choice_search_continents)
    await callback.answer()

# обработчик на нажатие кнопки с названием континента
@router.callback_query(ChoiceSearchCategoriesAndElements.choice_search_continents, F.data.startswith('button_continent_'))
async def print_search_continents(callback: types.CallbackQuery, state: FSMContext):
    continentCaption = callback.data.replace('button_continent_', '')

    user_data = await state.get_data()
    wiki_query = continentCaption + " " + user_data.get("chosen_search_category")

    await callback.message.answer(f'Твой запрос \"{wiki_query}\"')

    # обработка запроса в Википедию
    wikipedia.set_lang('ru')
    await callback.message.answer(f'Уже ищу в Википедии про {wiki_query}!\nПодожди чуть-чуть, пожалуйста.')
    wiki_results = wikipedia.search(wiki_query)
    if not wiki_results:
        await callback.message.answer('Ничего не найдено. Повторим?', reply_markup=kb_wiki)
    else:
        page_wiki = wikipedia.page(wiki_results[0])
        await callback.message.answer('Вот, что я нашел')
        await callback.message.answer(page_wiki.summary[:200])
        await callback.message.answer('Вот, где об этом указано')
        await callback.message.answer(page_wiki.url)

    await callback.message.answer("Продолжим поиск?", reply_markup=kb_inline_search_continents)

    await callback.answer()

# обработчик на команды info, help
@router.message(F.text.lower() == 'информация')
@router.message(F.text.lower() == 'помощь')
@router.message(F.text.lower() == 'info')
@router.message(F.text.lower() == 'help')
@router.message(Command("info"))
@router.message(Command("help"))
async def cmd_info(message: types.Message):
    command_list = "/start - запуск бота\n" \
                   "/info, /help - описание бота\n" \
                   "/search - поиск в Википедии"
    await message.answer(f"Доступные команды:\n{command_list}")

# обработчик на необработанное cообщение
@router.message(F.text)
async def msg_any(message: types.Message):
    await message.answer('Я тебя не понял!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())