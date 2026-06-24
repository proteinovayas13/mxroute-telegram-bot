import os
import requests
from datetime import datetime
from dotenv import load_dotenv
import os.path

# Указываем путь к .env явно
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

# Конфигурация
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
WEBMAIL_URL = os.getenv('WEBMAIL_URL')
MX_SERVER = os.getenv('MX_SERVER')
MX_USERNAME = os.getenv('MX_USERNAME')

print(f"Токен найден: {bool(TELEGRAM_BOT_TOKEN)}")
print(f"Chat ID найден: {bool(TELEGRAM_CHAT_ID)}")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML',
        'disable_web_page_preview': True
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            print(" Сообщение отправлено!")
            return True
        else:
            print(f" Ошибка: {response.text}")
            return False
    except Exception as e:
        print(f" Ошибка: {e}")
        return False

def get_webmail_message():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"""
 MXroute Webmail

 <a href="{WEBMAIL_URL}">Войти в почту</a>

 Сервер: {MX_SERVER}
 Логин: {MX_USERNAME}
 Пароль: (ваш пароль)

 Обновлено: {now}
    """
    return message

def main():
    print(" Запуск бота...")
    
    if not TELEGRAM_BOT_TOKEN:
        print(" Ошибка: TELEGRAM_BOT_TOKEN не найден в .env")
        print("Проверьте файл .env в папке:", os.path.dirname(__file__))
        return
    
    if not TELEGRAM_CHAT_ID:
        print(" Ошибка: TELEGRAM_CHAT_ID не найден в .env")
        return
    
    message = get_webmail_message()
    send_telegram_message(message)

if __name__ == "__main__":
    main()
