import requests

# Отправляем GET-запрос к API с параметром userId=1
response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})

# Проверяем статус-код (200 - успешно)
print("Статус-код ответа:", response.status_code)

# Выводим полученные записи в формате JSON
print("\nПолученные записи:")
posts = response.json()
for post in posts:
    print(post)