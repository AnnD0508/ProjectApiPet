import json
from settings import BASE_URL

class BaseApi:
    """API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self) -> json:
        self.base_url = BASE_URL
