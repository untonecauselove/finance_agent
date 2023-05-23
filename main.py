import requests
from creds import API_KEY


#base_currency = ""

# URL эндпоинта API и параметры запроса
url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"

# GET-запрос к API
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    data = response.json()
    # Обработка полученных данных
    # Вывод курсов валют
    print("USD Rate:", data["rates"]["USD"])
    print("RUB Rate:", data["rates"]["RUB"])
    print("EUR Rate:", data["rates"]["EUR"])
    print("GEL Rate:", data["rates"]["GEL"])
else:
    print("Ошибка при выполнении запроса:", response.status_code)