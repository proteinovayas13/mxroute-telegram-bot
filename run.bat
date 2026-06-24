@echo off
cd /d C:\Users\user\mxroute-telegram-bot
call venv\Scripts\activate
set HTTP_PROXY=http://proxy:port
set HTTPS_PROXY=http://proxy:port
python bot.py
