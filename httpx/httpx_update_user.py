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


headers_patch_user = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

body_patch_user = {
  "email": get_random_email(),
  "lastName": "SuperLex",
  "firstName": "LexLexLex",
  "middleName": "string2"
}

try:
    patch_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_data['user']['id']}", headers=headers_patch_user, json=body_patch_user)
    patch_user_response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f'К сожалению, Илья, ты ошибся, была вызвана ошибка {e}')
else:
    print(patch_user_response.status_code)
    print(patch_user_response.json())
    print(f"Задание выполнено, созданный пользователь был изменен: с {create_user_data['user']['email']} на {patch_user_response.json()['user']['email']}")
finally:
    print("Выполнение скрипта заверешно")