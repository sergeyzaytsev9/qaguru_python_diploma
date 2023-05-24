import json
from faker import Faker


class ScloudLK:

    def __init__(self, session):
        self.session = session
        self._authorization_cookie = None

    def get_token(self, login, password):
        return self.session.post(
            url="getJwtTokenPair",
            data={"login": login, 'password': password},
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'},
            allow_redirects=False
        )

    @property
    def auth_token(self):
        return self._authorization_cookie

    @auth_token.setter
    def auth_token(self, response):
        json_data = json.loads(response.text)
        self._authorization_cookie = json_data["data"]["access"]

    def get_gb_details(self, **kwargs):
        auth_token = kwargs.get('token', None)
        headers = {
            'Authorization': f"Bearer {auth_token}",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'}
        response = self.session.get('getGbDetails', headers=headers)
        return response

    def get_bases_list(self, **kwargs):
        auth_token = kwargs.get('token', None)
        headers = {
            'Authorization': f"Bearer {auth_token}",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'}
        response = self.session.get('getBasesList', headers=headers)
        return response

    def create_empty_base1C(self, **kwargs):
        auth_token = kwargs.get('token', None)
        fake = Faker('en_US')
        infobase_name = fake.name().replace(" ", "")

        headers = {
            'Authorization': f"Bearer {auth_token}",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'}
        data = {'baseName': infobase_name, 'typeId': '26554773'}
        response = self.session.post('createBase1C', headers=headers, data=data)
        return response


    def get_ticket_list(self, **kwargs):
        auth_token = kwargs.get('token', None)

        headers = {
            'Authorization': f"Bearer {auth_token}",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'}
        data = {
            'ticketState': 'Any',
            'periodStartDate': '2023-04-16',
            'periodEndDate': '2023-04-17'}
        response = self.session.post('getTicketListBpm', headers=headers, data=data)
        return response

