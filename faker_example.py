from faker import Faker

faker = Faker("ru_RU")

print(faker.name())
print(faker.address())
print(faker.email())

data = {
    "name": faker.name(),
    "email": faker.email(),
    "age": faker.random_int(min=10, max=100)
}

print(data)