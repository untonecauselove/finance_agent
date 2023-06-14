from exchange_rates import *
from telegram.ext import Updater, CommandHandler
import telegram_backend
from creds import TG_TOKEN, IS_DEBUG

# Дебаг мод
if IS_DEBUG:
    get_rates()


# Экземпляр updater.dispatcher для передачи команд
updater = Updater(token=TG_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Регистрация обработчиков команд
dispatcher.add_handler(CommandHandler("start", telegram_backend.start))
dispatcher.add_handler(CommandHandler("rates", telegram_backend.get_exchange_rates))
dispatcher.add_handler(CommandHandler("mybalance", telegram_backend.get_my_balance))

# Запуск бота
updater.start_polling()