import httpx


from tools.fakers import fake
create_user_payload = {
  "email": fake.email(),
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


del_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
try:
    del_user_response = httpx.delete(f"http://localhost:8000/api/v1/users/{create_user_data['user']['id']}", headers=del_user_headers)
    del_user_response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f'К сожалению, Илья, ты ошибся, была вызвана ошибка {e}')
else:
    print(del_user_response.status_code)
    print(del_user_response.json())
    print(f"Задание выполнено, был удален пользователь:{create_user_data['user']['email']}")
finally:
    print("Выполнение скрипта заверешно")