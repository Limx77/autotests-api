# from clients.authentication.authentication_schema import TokenSchema
#
# print(TokenSchema.model_json_schema())
#
# schema = {'description': 'Описание структуры аутентификационных токенов.',
#           'properties': {
#               'tokenType': {'title': 'Tokentype', 'type': 'string'},
#               'accessToken': {'title': 'Accesstoken', 'type': 'string'},
#               'refreshToken': {'title': 'Refreshtoken', 'type': 'string'}
#           },
#           'required': ['tokenType', 'accessToken', 'refreshToken'],
#           'title': 'TokenSchema',
#           'type': 'object'}

from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
import jsonschema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
  email = get_random_email(),
  password = "string",
  last_name = "string",
  first_name = "string",
  middle_name = 'string')

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)

