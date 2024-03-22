from data.data_models import Person
from faker import Faker

def generated_person():
    faker = Faker()
    yield Person(
        full_name=faker.first_name() + ' ' + faker.last_name(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address()
    )
