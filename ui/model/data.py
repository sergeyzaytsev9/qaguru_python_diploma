from faker import Faker
from enum import Enum
from typing import Literal, List
from dataclasses import dataclass


@dataclass
class Service:
    service_name: str
    configuration_names: List[str]
    count_sessions: int
    summary_count_sessions: str
    count_infobases: int
    summary_count_infobases: str
    has_configurator: str


fresh_tariff = Service(
    service_name='fresh',
    configuration_names=
    [
        '1С: Управление нашей фирмой'
    ],
    count_sessions=5,
    count_infobases=5,
    has_configurator='true',
    summary_count_sessions='5',
    summary_count_infobases='14',

)


fake = Faker('en_US')
email_random = fake.email()
fake_login = fake.name().replace(" ", "")
fake_password = fake.random.randint(3, 10)
text_random = fake.text()
comment = fake.text()




