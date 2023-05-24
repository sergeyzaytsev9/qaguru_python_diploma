import os

from api.helpers.requests_helper import BaseSession


def scloud() -> BaseSession:
    api_url = os.getenv('api_url')
    return BaseSession(base_url=api_url)
