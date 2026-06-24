import os
import time
from datetime import datetime
import subprocess
import sys

def send_message():
    """Запуск bot.py"""
    result = subprocess.run([sys.executable, "bot.py"], capture_output=True, text=True)
    print(f"[{datetime.now()}] {result.stdout}")
    if result.stderr:
        print(f"Ошибка: {result.stderr}")

if __name__ == "__main__":
    send_message()
