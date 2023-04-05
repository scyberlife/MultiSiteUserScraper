from requests import get
from json import dump
from aiogram import types
from config import bot
from bs4 import BeautifulSoup

all_url = {
      "github": "https://github.com/",
      "career.habr": "https://career.habr.com/",
      "tiktok": "https://www.tiktok.com/@",
      "pikabu": "https://pikabu.ru/@",
      "reddit": "https://reddit.com/user/",
      "instagram": "https://instagram.com/",
 }

async def all_search(message: types.Message):
    # Получаем имя пользователя, которое нужно найти
    username = message.text.split('/search ')[1]
    # Создаем пустой словарь для хранения результатов
    search_results = {}

    # В цикле по сайтам проверяем, найден ли пользователь и сохраняем результаты в словарь
    for url in all_url.values():
        try:
            response = get(url + username, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            # user_info = soup.find('div', {'class': 'имя_класса'})
            user_info = soup.find('a', class_='_31VWB3vSkv19o3I7RVE710')
            user_info1 = soup.find('title')
        except:
            continue
        wrong = 'Sorry, nobody on Reddit goes by that name.'
        if username in str(user_info) or username in str(user_info1):
            if username not in search_results:
                search_results[username] = []
            search_results[username].append(f"{url}{username}")


    # Сохраняем результаты поиска в файл JSON
    with open('search_results.json', 'w') as f:
        dump(search_results, f, indent=4)

    # Формируем сообщение с результатами поиска
    message_text = f"Результаты поиска для пользователя {username}:\n\n"
    for url in search_results.get(username, []):
        message_text += f"{url}\n"
    await bot.send_message(chat_id=message.chat.id, text=message_text)