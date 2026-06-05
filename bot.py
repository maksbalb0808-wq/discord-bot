import time
import requests
import random
from datetime import datetime, timedelta

# ================= НАСТРОЙКИ =================
TOKEN = "СЮДА_ВСТАВЬТЕ_ТОКЕН_ИЗ_БРАУЗЕРА"
CHANNEL_ID = "СЮДА_ВСТАВЬТЕ_ID_ПОЛЬЗОВАТЕЛЯ"
MESSAGE = "Доброе утро! Это автоматическое сообщение."
# =============================================

headers = {
    "Authorization": TOKEN, 
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("Скрипт вечной ежедневной отправки запущен в облаке Koyeb.")

while True:
    now = datetime.now()
    
    # На Koyeb время тоже UTC. 4:00 утра по МСК — это 01:00 ночи по UTC.
    base_target = now.replace(hour=1, minute=0, second=0, microsecond=0)
    
    # ЗАЩИТА: Рандомное смещение времени (от 1 до 5 минут)
    random_minutes = random.randint(1, 5)
    random_seconds = random.randint(0, 59)
    target_time = base_target + timedelta(minutes=random_minutes, seconds=random_seconds)
    
    if now >= target_time:
        base_target += timedelta(days=1)
        target_time = base_target + timedelta(minutes=random_minutes, seconds=random_seconds)
    
    print(f"Следующее сообщение запланировано на: {target_time.strftime('%Y-%m-%d %H:%M:%S')} (по UTC)")
    
    # Ожидание нужного времени
    while datetime.now() < target_time:
        time.sleep(10)
        
    print("Время пришло. Имитируем действия человека...")
    
    try:
        # ЗАЩИТА: Статус "Печатает..."
        typing_url = f"https://discord.com{CHANNEL_ID}/typing"
        requests.post(typing_url, headers=headers, timeout=10)
        
        # ЗАЩИТА: Имитация ввода текста (от 6 до 12 секунд)
        time.sleep(random.randint(6, 12))
        
        # Отправка
        msg_url = f"https://discord.com{CHANNEL_ID}/messages"
        payload = {"content": MESSAGE}
        response = requests.post(msg_url, json=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("Сообщение успешно доставлено!")
        else:
            print(f"Ошибка! Код сервера Discord: {response.status_code}")
            
    except Exception as e:
        print(f"Сетевая ошибка: {e}")
        
    # Спим 5 минут, чтобы избежать повтора в ту же минуту
    time.sleep(300)
