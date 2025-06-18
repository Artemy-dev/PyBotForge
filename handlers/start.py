import sqlite3
import os
from telebot.types import Message

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message: Message):
        telegram_id = message.from_user.id
        conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../db/users.db'))
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO users (telegram_id) VALUES (?);", (telegram_id,))
        conn.commit()
        conn.close()
        bot.send_message(message.chat.id, "Hello!")
