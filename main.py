import requests

# Отправляем GET-запрос к API GitHub для поиска репозиториев с кодом html
response = requests.get('https://api.github.com/search/repositories', params={'q': 'html'})

# Печатаем статус-код ответа
print("Статус-код ответа:", response.status_code)

# Печатаем содержимое ответа в формате JSON
print("Содержимое ответа:")
print(response.json())