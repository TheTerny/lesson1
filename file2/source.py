import json
import random
from datetime import datetime
import time
import sched
import os

# Класс для статьи
class Article:
    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.datetime = datetime.now().strftime("%A %d-%b-%Y %H:%M:%S") 
        self.likes = random.randint(10, 100)

# Глобальные настройки
_I = 5  # Количество итераций
_TIME_SEC = 10  # Интервал между итерациями в секундах
_LOG_DIR = 'json/log'
_DOWNLOAD_DIR = 'json/download'
_LOG_FILE = f'{_LOG_DIR}/serialize-{datetime.now().strftime("%Y%m%d")}.log'

# Создание директорий при необходимости
os.makedirs(_LOG_DIR, exist_ok=True)
os.makedirs(_DOWNLOAD_DIR, exist_ok=True)

# Логирование
def log(message):
    with open(_LOG_FILE, "a") as f:
        f.writelines(f'{datetime.now().strftime("%H:%M:%S")} | {message} \n')

# Преобразование объекта в словарь для сериализации
def to_dict(obj):
    result = obj.__dict__
    result["className"] = obj.__class__.__name__
    return result

# Функция для записи JSON данных
def send_json_data(index):
    try:
        # Генерация данных статьи
        title = f'Заголовок - {random.randint(1, 9999)}'
        body = f'Некоторый текст - {random.randint(1000, 9999999)}'
        article = Article(title, body)
        
        # Формирование имени файла
        filename = f'{_DOWNLOAD_DIR}/{index}-{datetime.now().strftime("%Y%m%d%H%M%S")}-data.json'
        
        # Запись данных в файл
        with open(filename, "w") as f:
            json.dump(article, f, default=to_dict, indent=4, ensure_ascii=False)
        
        log(f'Отправка {index} выполнена: {filename}')
        print(f'Данные сохранены: {filename}')
    except Exception as err:
        log(f'Ошибка отправки {index} - {err}')
        print(f'Ошибка записи данных: {err}')

# Инициализация счетчика
_J = 0

# Функция для выполнения работы
def do_work(sc): 
    global _J
    _J += 1
    print(f'--- {_J} ---')
    send_json_data(_J)
    
    # Условие продолжения работы
    if _J < _I:
        sc.enter(_TIME_SEC, 1, do_work, (sc,))

# Основная программа
log("-= START =-")
s = sched.scheduler(time.time, time.sleep)
s.enter(1, 1, do_work, (s,))
s.run()
log("-= STOP =-")