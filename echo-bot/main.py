# импортируем необходимые модули библиотеки aiogram

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import Token

# cоздаем объект бота и передаем в него наш токен
bot = Bot(token=Token)

# В аiogram хендлерами управляет диспечер. Создаем объект диспечер и передаем в нашего бота
dp = Dispatcher(bot)


# В аiogram хендлерами управляет диспечер. Создаем объект диспечер и передаем в нашего бота
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply('ПРивет я эхо бот. напиши мне что нибудь')


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply('Просто напиши что нибудь')


# оборачиваем диспечер, управляющим хендлером, в декаратор, внутри которой будет асинхроная функция ловящаявсе все текстовые сообщения и отсылает их обратноет
@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


# запускаем бота
# создаем условие. вызываем у executor метод start_polling  и передаем в него объект класса диспечер
if __name__ == '__main__':
    executor.start_polling(dp)
