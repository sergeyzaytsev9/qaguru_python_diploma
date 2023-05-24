import os
import allure
from dotenv import load_dotenv
from api.model.scloudlk import ScloudLK
from pytest_voluptuous import S
from api.schemas.schemas import SUCCESSFUL, create_base,get_bases_list,get_gb_details
from api.helpers.requests_helper import response_loads

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

@allure.tag("API")
@allure.label('owner', 'zaytsev')
@allure.feature('API')
@allure.story('Bases')
def test_get_gb_details(scloud):
    """Получение информаци о размере диска"""
    scloud = ScloudLK(scloud)
    scloud.auth_token = scloud.get_token(login=LOGIN, password=PASSWORD)

    response = scloud.get_gb_details(token=scloud.auth_token)
    response_success = response_loads(response)["success"]

    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'
    assert S(get_gb_details) == response.json()
    assert response_success == True, f'Response should be true'


@allure.tag("API")
@allure.label('owner', 'zaytsev')
@allure.feature('API')
@allure.story('Bases')
def test_get_bases_list(scloud):
    """Получение информаци об информационных базах"""
    scloud = ScloudLK(scloud)
    scloud.auth_token = scloud.get_token(login=LOGIN, password=PASSWORD)

    response = scloud.get_bases_list(token=scloud.auth_token)
    response_successful = response_loads(response)["success"]

    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'
    assert S(get_bases_list) == response.json()
    assert response_successful == True, f'Response should be true'


@allure.tag("API")
@allure.label('owner', 'zaytsev')
@allure.feature('API')
@allure.story('Bases')
def test_create_empty_base1C(scloud):
    """Создание пустой базы для разработки"""
    scloud = ScloudLK(scloud)
    scloud.auth_token = scloud.get_token(login=LOGIN, password=PASSWORD)

    response = scloud.create_empty_base1C(token=scloud.auth_token)
    response_message = response_loads(response)["data"]["message"]
    response_success = response_loads(response)["success"]

    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'
    assert S(create_base) == response.json()
    assert response_message == 'База будет создана в течении 4 минут'
    assert response_success == True, f'Response should be true'