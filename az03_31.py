import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL-адрес веб-сайта, с которого будет производиться поиск
url = 'https://www.divan.ru/sankt-peterburg/category/divany-i-kresla'

# Отправлен GET-запрос к веб-сайту
response = requests.get(url)

# Проверка, успешно ли выполнен запрос
if response.status_code == 200:
    # Разбираем содержимое HTML с помощью BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Найти соответствующие элементы, содержащие цены
    # Примечание: Обновить селекторы в соответствии с фактической структурой сайта
    prices = []
    for price_tag in soup.select('div.price'):
        price_text = price_tag.get_text(strip=True)
        # Удалить нечисловые символы, кроме десятичных точек
        price_text = price_text.replace(' ', '').replace(',', '.').replace('р', '').replace('₽', '')
        print(price_text)
        try:
            price = float(price_text)
            prices.append(price)
        except ValueError:
            continue

    # Проверить, были ли найдены какие-либо цены
    if prices:
        # Преобразуем цены в DataFrame
        df_prices = pd.DataFrame(prices, columns=['Price'])

        # Сохранить в CSV-файл
        df_prices.to_csv('sofa_prices.csv', index=False)

        # Рассчитать среднюю цену
        average_price = df_prices['Price'].mean()
        print(f'Средняя цена диванов: {average_price:.2f}')

        # Create a histogram of prices
        plt.hist(df_prices['Price'], bins=30, edgecolor='black')
        plt.title('Гистограмма цен на диваны')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print("Цены на сайте не найдены.")
else:
    print(f"Не удалось получить веб-страницу. Код состояния: {response.status_code}")
