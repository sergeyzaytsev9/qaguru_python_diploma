import json
import logging

from requests import Session
import curlify
import allure


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        with allure.step(f'{method} {url}'):
            response = super().request(method, url=f'{self.base_url}{url}', **kwargs)
            message = curlify.to_curl(response.request)
            logging.info(f'{response.status_code} {message}')
            with allure.step(f'{response.request.method} {response.request.url}'):
                allure.attach(
                    body=message.encode('utf8'),
                    name=f'Request {method} {response.status_code}',
                    attachment_type=allure.attachment_type.TEXT,
                    extension='txt'
                )
                try:
                    allure.attach(
                        body=json.dumps(response.json(), indent=4, ensure_ascii=False).encode('utf8'),
                        name=f'Response {response.request.method}',
                        attachment_type=allure.attachment_type.JSON,
                        extension='json'
                    )
                except ValueError as error:
                    allure.attach(
                        body=response.text.encode('utf8'),
                        name=f'NOT Json Response {response.request.method}',
                        attachment_type=allure.attachment_type.JSON,
                        extension='json'
                    )
        return response

def response_loads(body):
    json_data = json.loads(body.text)
    return json_data