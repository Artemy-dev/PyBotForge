# 🚀 [PyBotForge](https://github.com/Artemy-dev/PyBotForge) — Telegram Bot Template for Python  
A basic, clean template for creating Telegram bots with pyTelegramBotAPI. Fast start without boilerplate.  
(Базовый шаблон для Telegram-ботов на Python с pyTelegramBotAPI. Быстрый старт без лишней возни.)

---

## 💻 Supported Platforms

- ✅ Windows  
- ✅ macOS  
- ✅ Linux  

---

## 📦 Features / Возможности

- 🔹 Clean and logical project structure (Django-style) / Чистая и логичная структура проекта (в стиле Django)  
- 🔹 Environment variables support (.env) / Поддержка переменных окружения `.env`  
- 🔹 User storage with SQLite / Хранение пользователей в SQLite  
- 🔹 Modular command handlers / Модульные обработчики команд  
- 🔹 Easily extendable for any task / Легко расширяется под любую задачу

---

## ❓ Why this project? / Зачем этот проект?

This template helps to quickly start Telegram bot development without spending time on setup and boilerplate code.  
Шаблон помогает быстро начать разработку Telegram-бота без траты времени на настройку и шаблонный код.

---

## 🚀 Installation / Установка

```bash
git clone https://github.com/Artemy-dev/PyBotForge.git
cd PyBotForge
pip install pyTelegramBotAPI python-dotenv
````

---

## ⚙️ Usage / Пример использования

1. Create/edit `.env` file with your bot token:

```
BOT_TOKEN=your_bot_token
```

2. Run the bot:

```bash
python bot.py
```

---

## 📁 Project Structure / Структура проекта

```
├── db/                # Работа с БД
│   ├── __init__.py
│   └── users.db       # Хранилище Telegram ID пользователей
├── handlers/          # Обработчики команд
│   ├── __init__.py
│   └── start.py       # /start — приветствие и добавление пользователя в БД
├── utils/             # Вспомогательные функции
│   └── __init__.py
├── .env               # Переменные окружения (токен и т.д.)
├── bot.py             # Точка входа: запуск бота
├── config.py          # Загрузка и хранение конфигураций из .env
└── keyboards.py       # Клавиатуры (Reply / Inline)
```

---

## 👤 Author / Автор

**Artem Grachev**<br>
Python/Golang Developer | ML & DevOps Enthusiast<br>
Telegram: [@Artemy\_Develop](https://t.me/Artemy_Develop)<br>
GitHub: [Artemy-dev](https://github.com/Artemy-dev)

---

## 🌍 SEO Keywords

* telegram bot template
* pytelegrambotapi example
* python telegram bot starter
* sqlite telegram bot
* modular telegram handlers
* dotenv python bot
* telegram bot boilerplate
* telegram bot cli python
