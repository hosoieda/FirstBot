1. Создание виртуального окружения: 
```python -m venv venv```
2. Чтобы начать пользоваться виртуальным окружением, необходимо его активировать
```venv\Scripts\activate.bat``` для Windows;
```source venv/bin/activate``` для Linux и MacOS.
3. Установка зависимостей:
```pip install -r requirements.txt```
4. Команда создания файла .env
```cp .example.env .env```
5. Регистрация бота:
Нужно найти бота @BotFather, написать ему /start, или /newbot, 
заполнить поля, которые он спросит (название бота и его короткое 
имя), и получить сообщение с токеном бота и ссылкой на 
документацию. Токен нужно сохранить, желательно надёжно, 
так как это единственный ключ для авторизации бота и 
взаимодействия с ним.
6. Поместите токен бота в переменную BOT_TOKEN в файле .env
7. Чтобы запустить проект, пропишите в терминале:
```python boy.py```
8. Найдите своего бота в телеграм и запустите его командой /start