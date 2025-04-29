import requests

# Данные для отправки (новый пост)
new_post = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправляем POST-запрос
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)

# Выводим статус-код (201 - Created, если успешно)
print("Статус-код ответа:", response.status_code)

# Выводим содержимое ответа (созданная запись)
print("\nОтвет сервера (созданный пост):")
print(response.json())