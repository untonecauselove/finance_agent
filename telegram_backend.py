from telegram.ext import Updater, CommandHandler
import exchange_rates

# Функция-обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для получения курса валют. Введите /курс для получения курса валют.")

# Функция-обработчик команды /курс
def get_exchange_rates(update, context):
    rates = exchange_rates.get_rates()
    if rates:
        message = f"Курсы валют:\nUSD: {rates['USD']}\nRUB: {rates['RUB']}\nEUR: {rates['EUR']}\nGEL: {rates['GEL']}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ошибка при получении курсов валют.")

# Создание экземпляра Updater и передача токена вашего бота
updater = Updater(token="TOKEN", use_context=True)

# Получение диспетчера для регистрации обработчиков команд
dispatcher = updater.dispatcher

# Регистрация обработчиков команд
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("rates", get_exchange_rates))

# Запуск бота
updater.start_polling()