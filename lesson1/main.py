import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random

# включаем логгирование
logging.basicConfig(level=logging.INFO)

# создаем объект бота
bot = Bot(token=config.token)

# диспетчер
dp = Dispatcher()

# обработчик на команду start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    name = message.chat.ﬁrst_name
    command_list = "/start - запуск бота\n" \
                   "/info - описание бота\n" \
                   "/number - угадай число от 1 до 10"
    await message.answer(f"Привет, {name}!\nДоступные команды:\n{command_list}")

# обработчик на команду info
@dp.message(F.text.upper() == 'ИНФОРМАЦИЯ')
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.reply("Я твой первый бот в Telegram! 😊\nУгадай число от 1 до 10!")

@dp.message(Command("number"))
async def cmd_number(message: types.Message):
    number = random.randint(1,10)
    await message.answer(f"Я загадал число {number}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())