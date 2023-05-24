import os
import allure
from dotenv import load_dotenv
from api.model.scloudlk import ScloudLK
from api.schemas.schemas import SUCCESSFUL
from api.helpers.requests_helper import response_loads

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


@allure.tag("API")
@allure.label('owner', 'zaytsev')
@allure.feature('API')
@allure.story('Tickets')
def test_get_ticket_list(scloud):
    """Получение списка всех тикетов"""
    scloud = ScloudLK(scloud)
    scloud.auth_token = scloud.get_token(login=LOGIN, password=PASSWORD)

    response = scloud.get_gb_details(token=scloud.auth_token)
    response_success = response_loads(response)["success"]

    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'
    assert response_success == True, f'Response should be true'