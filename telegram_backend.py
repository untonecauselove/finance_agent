import exchange_rates
import clickhouse_backend


# Функция-обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для получения курса валют. Введите /курс для получения курса валют.")

# Функция-обработчик rates
def get_exchange_rates(update, context):
    rates = exchange_rates.get_rates().to_dict('dict')
    if rates:
        message = f"Курсы валют:\nUSD: {rates['USD']}\nRUB: {rates['RUB']}\nEUR: {rates['EUR']}\nGEL: {rates['GEL']}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        clickhouse_backend.write_df_to_clickhouse(rates, 'myrates.actual_rates')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ошибка при получении курсов валют.")

# Функция-обработчик balance
def get_my_balance(update, context):
    bal = clickhouse_backend.get_from_clickhouse('myrates.actual_balance')
    if bal:
        message = f"Мой баланс:\nUSD: {bal['USD']}\nRUB: {bal['RUB']}\nEUR: {bal['EUR']}\nGEL: {bal['GEL']}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ошибка при получении баланса")
