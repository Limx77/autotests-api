import httpx


from tools.fakers import get_random_email
create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post('http://localhost:8000/api/v1/users', json = create_user_payload)
create_user_data = create_user_response.json()
print(create_user_response.status_code)
print(create_user_response.json())


login_payload = {
  "email": f"{create_user_data['user']['email']}",
  "password": "string"
}
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json = login_payload)
login_response_data = login_response.json()
print(login_response.status_code)
print(login_response.json())


get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
try:
    get_user_response = httpx.get(f"http://localhost:8000/api/v1/users/{create_user_data['user']['id']}", headers=get_user_headers)
    get_user_response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f'К сожалению, Илья, ты ошибся, была вызвана ошибка {e}')
else:
    print(get_user_response.status_code)
    print(get_user_response.json())
    print("""Красава! Ты правильно выполнил задание и смог написать\nзапросы на создание юзера, достать токен и выполнить GET запрос!
""")
finally:
    print("Выполнение скрипта заверешно")



