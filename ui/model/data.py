from faker import Faker
from typing import List
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
        '1С: Управление нашей фирмой',
        '1С: Зарплата и управление персоналом ПРОФ'
    ],
    count_sessions=5,
    count_infobases=5,
    has_configurator='true',
    summary_count_sessions='10',
    summary_count_infobases='15'
)


fake = Faker('en_US')
fake_login = fake.name().replace(" ", "")
fake_password = fake.random.randint(3, 10)




