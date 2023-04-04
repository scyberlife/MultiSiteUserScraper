from aiogram.utils import executor
from commands import all_search
from config import bot, dp


if __name__ == '__main__':
    dp.register_message_handler(all_search, commands=['search'])
    executor.start_polling(dp, skip_updates=True)
