import time
import requests
import random
from datetime import datetime

# ================= НАСТРОЙКИ (ЗАПОЛНИТЕ СВОИ ДАННЫЕ) =================
TOKEN = "MTUxMTk5NDgzNjc5MjY0MzU4Ng.Gf96Ki.s0REHDT4J4jnP6-ZJ0QcwK0rl2n3qkpoEQfuKs"
CHANNEL_ID = "1221881016948621356"
MESSAGE = "Доброе утро! Это автоматическое сообщение."
# =====================================================================

# ЗАЩИТА №1: Маскировка под реальный браузер Google Chrome на Windows 10
headers = {
    "Authorization": TOKEN, 
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print(f"[{datetime.now().strftime('%H:%M:%S')}] Сервер запущен платформой Render.")

# ЗАЩИТА №2: Случайное смещение минут и секунд.
# Скрипт проснется в 4:00, но сознательно замерзнет на случайное время от 1 до 5 минут.
random_minutes = random.randint(1, 5)
random_seconds = random.randint(0, 59)
total_delay_seconds = (random_minutes * 60) + random_seconds

print(f"Применяем маскировку времени. Задержка составит: {random_minutes} мин. {random_seconds} сек.")
print(f"Сообщение уйдет примерно в 04:{random_minutes:02d} утра по МСК.")

# Скрипт уходит в ожидание
time.sleep(total_delay_seconds)

print("Время задержки истекло. Начинаем имитацию действий человека...")

try:
    # ЗАЩИТА №3: Отправляем в Discord статус «Печатает...»
    typing_url = f"https://discord.com{CHANNEL_ID}/typing"
    requests.post(typing_url, headers=headers, timeout=10)
    
    # ЗАЩИТА №4: Ждем от 6 до 13 секунд (имитируем реальную скорость набора текста руками)
    human_typing_speed = random.randint(6, 13)
    print(f"Имитируем ввод текста в течение {human_typing_speed} сек...")
    time.sleep(human_typing_speed)
    
    # ОТПРАВКА СООБЩЕНИЯ
    msg_url = f"https://discord.com{CHANNEL_ID}/messages"
    payload = {"content": MESSAGE}
    response = requests.post(msg_url, json=payload, headers=headers, timeout=10)
    
    if response.status_code == 200:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Сообщение успешно доставлено жителю чата!")
    else:
        print(f"Ошибка! Сервер Discord вернул код: {response.status_code}. Ответ: {response.text}")
        
except Exception as e:
    print(f"Произошел сетевой сбой при отправке: {e}")

print("Работа скрипта на сегодня завершена. Сервер отключается.")
