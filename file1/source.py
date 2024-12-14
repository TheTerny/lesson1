import datetime
import json
import random
import os

# Путь для сохранения файлов
_DOWNLOAD_PATH = "Download/"
_N = 0  # Счетчик статей

# Проверка и создание директории для файлов
os.makedirs(_DOWNLOAD_PATH, exist_ok=True)

# Класс статьи
class Article:
    def __init__(self, name):
        self.name = name
        self.likes = random.randint(0, 100)
        self.created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Функция для записи статьи в JSON
def json_dump_article(art: Article):
    global _N
    _N += 1
    dt = datetime.datetime.now()
    dt_str = dt.strftime('%Y-%m-%d_%H-%M-%S')
    
    # Формирование пути и имени файла
    path = f'{_DOWNLOAD_PATH}{_N}_{dt_str}.json'
    try:
        # Запись в файл с заменой содержимого
        with open(path, 'w') as f:
            json.dump(art.__dict__, f, indent=4, ensure_ascii=False)
        print(f"Сохранено: {path}")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

# Функция для создания статьи
def get_article():
    art = Article(f"Article {random.randint(1000, 9999)}")
    return art

# Основная рабочая функция
def do_work():
    art = get_article()
    json_dump_article(art)

# Главный цикл
for i in range(10):
    do_work()

print('Все статьи успешно сохранены!')


