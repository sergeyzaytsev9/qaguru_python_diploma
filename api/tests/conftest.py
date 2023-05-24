import os
import pytest
from dotenv import load_dotenv
from api.helpers.requests_helper import BaseSession


@pytest.fixture(scope="session")
def scloud():
    load_dotenv()
    api_url = os.getenv('api_url')
    return BaseSession(base_url=api_url)

@pytest.fixture(scope='session', autouse=True)
def auto_env():
    load_dotenv()