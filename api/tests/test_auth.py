import os
import allure
from dotenv import load_dotenv
from api.model.scloudlk import ScloudLK
from api.schemas.schemas import SUCCESSFUL,token
from api.helpers.requests_helper import response_loads
from pytest_voluptuous import S


load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


@allure.tag("API")
@allure.label('owner', 'zaytsev')
@allure.feature('API')
@allure.story('Authorization')
def test_get_token(scloud):
    scloud = ScloudLK(scloud)

    response = scloud.get_token(login=LOGIN,password=PASSWORD)
    response_success = response_loads(response)["success"]

    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'
    assert S(token) == response.json()
    assert response_success == True, f'Response should be true'