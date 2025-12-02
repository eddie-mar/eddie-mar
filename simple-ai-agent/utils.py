import re
import os
from abc import ABC, abstractmethod

import requests
from dotenv import load_dotenv

import operations

load_dotenv()
key = os.getenv('OPEN_WEATHER_API_KEY')


class AbsFunc(ABC):
    @abstractmethod
    def execute(self):
        pass

class GetWeather(AbsFunc):
    def execute(self, args: dict) -> dict:
        if not isinstance(args, str):
            raise ValueError('args must be a dict')
        
        city = args.get('city')
        if not isinstance(city, str):
            raise ValueError('City must be a string')
        
        resp = requests.get("https://api.openweathermap.org/data/2.5/weather", params={"q": city, "appid": key}, timeout=3)
        resp.raise_for_status()
        data = resp.json()
        return {'temp': data.get('main').get('temp'), 'units': 'C'}

class RunMath(AbsFunc):
    def execute(self, args: str) -> float | int:
        if not isinstance(args, dict):
            raise ValueError('args must be a dict')
        
        expr = args.get('expression')
        if not isinstance(expr, str):
            raise ValueError('Expression must be a string')

        pattern = r"^\s*(\d+\.?\d*)\s*([+\-/*])\s*(\d+\.?\d*)\s*$"
        match = re.match(pattern, expr)
        if not match:
            raise ValueError('Invalid expression')
        a, operator, b = match.groups()

        try:
            a = float(a) if '.' in a else int(a)
            b = float(b) if '.' in b else int(b)
        except ValueError:
            raise ValueError('Variables must be numeric')

        if not isinstance(a, (int, float)) or not isinstance(b, int | float):
            raise ValueError('Variables are not valid')
        
        try:
            operator = operations.OperatorFactory().get(operator)
            return operator.calculate(a, b)
        except Exception as e:
            raise Exception(e)


class ToolFactory:
    @staticmethod
    def get(tool: str) -> AbsFunc:
        mapping = {
            'get_weather': GetWeather,
            'run_math': RunMath
        }
        try:
            return mapping[tool]()
        except KeyError:
            raise Exception('Unknown tool')