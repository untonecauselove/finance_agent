import requests
from creds import API_KEY, IS_DEBUG
import pandas as pd

def get_rates():

    # URL эндпоинта API и параметры запроса
    url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"

    # GET-запрос к API
    response = requests.get(url)

    # Проверка успешности запроса
    if response.status_code == 200:
        data = response.json()
        # Debug курсов валют
        if IS_DEBUG:
            print("USD Rate:", data["rates"]["USD"])
            print("RUB Rate:", data["rates"]["RUB"])
            print("EUR Rate:", data["rates"]["EUR"])
            print("GEL Rate:", data["rates"]["GEL"])

        try:
            df = pd.read_json(data)
            return df
        except ValueError as err:
            print("Ошибка при парсинге json", err.args)
            return 0
    else:
        raise ValueError("Ошибка при выполнении запроса:", response.status_code)
        return 0