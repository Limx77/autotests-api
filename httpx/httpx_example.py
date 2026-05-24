import httpx


# """Пример отправки GET запроса"""
#
# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
# print(response.status_code)
# print(response.json())
#
#
#
# """Пример отправки POST запроса"""
#
# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
# print(response.status_code)
# print(response.request.headers)
# print(response.json())
#
#
#
# """Пример отправки POST запроса с contatn-type не json, а data (application/x-www-form-urlencoded)"""
#
# data = {"username": "test_user", "password": "12345"}
# response = httpx.post('https://httpbin.org/post', data=data)
# print(response.status_code)
# print(response.request.headers)
# print(response.json())
#
#
#
# """Как в запросе передавать наши headers"""
#
# headers = {"Authorization": "Bearer my_test_token"}
# response = httpx.get('https://httpbin.org/get', headers=headers)
# print(response.status_code)
# print(response.request.headers)
# print(response.json())
#
#
#
# """Как в запросе передавать params"""
#
# params = {"userId": 1}
# response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
# print(response.status_code)
# print(response.request.headers)
# print(response.json())



# """Как в запросе передать файл"""
#
# files = {"file": ("example.txt", open("example.txt", 'rb'))}
# response = httpx.post('https://httpbin.org/post', files=files)
# print(response.status_code)
# print(response.request.headers)
# print(response.json())



# """Работа с сессиями"""
#
# with httpx.Client() as client:
#     response1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
#     response2 = client.get('https://jsonplaceholder.typicode.com/todos/2')
# print(response1.json())
# print(response2.json())



# """Тут пример как через Client можно задать нужные headers
# после чего при всех дальнийших вызовах через client во всех запросах
# будет использоваться указанный headers
# """
#
# cli =  httpx.Client(headers={"Authorization": "Bearer my_test_token"})
# response = cli.get("https://httpbin.org/get")
#
# print(response.json())



"""Как работать с ошибками в HTTPX"""

try:
    response = httpx.get('https://jsonplaceholder.typicode.com/invalid-url')
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")



"""Как работать с ошибками задержки, если сервер
отвечает дольше положенного времени
"""
try:
    response = httpx.get('https://httpbin.org/delay/5', timeout=2)
except httpx.ReadTimeout as e:
    print("Запрос превысил лимит времени")
