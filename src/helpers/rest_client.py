
from typing import Union
from json.decoder import JSONDecodeError
from src.models.response import Response
import requests


class RestClient:
    headers = {"Content-type": "application/json", "Accept": "text/plain"}

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get(self, resource: str, query_params: Union[str, None]) -> Response:
        url = f"{self.base_url}/{resource}?{query_params or ''}"
        response = requests.get(url, headers=self.headers)
        status_code = response.status_code
        response = Response(
            status_code=status_code,
            data=self.__get_response(response)
        )
        return response

    @classmethod
    def __get_response(cls, response: Response) -> Union[str, dict]:
        try:
            content = response.json()
        except JSONDecodeError:
            content = response.text
        return content