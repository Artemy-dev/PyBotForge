import telebot
from config import TOKEN
from handlers import start

bot = telebot.TeleBot(TOKEN)

# Регистрируем все обработчики
start.register_handlers(bot)

# Запускаем бота
if __name__ == "__main__":
    print("Bot is polling...")
    bot.infinity_polling()
