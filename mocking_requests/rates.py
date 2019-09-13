import requests


RATES_API_URL = 'https://api.exchangeratesapi.io/latest'


def get_rate(base, to):
    response = requests.get(RATES_API_URL, params={'base': base})
    if response.status_code != 200:
        return None

    data = response.json()
    return data['rates'][to]
