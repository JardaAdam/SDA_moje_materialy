import requests

class NotFoundExeption(Exception):
    pass


def get_residents_count(planet_url):
    response = requests.get(planet_url)
    if response.status_code == 404:
            raise NotFoundExeption("Planet not found")

    data = response.json()
    return len(data['residents'])


url = 'http://swapi.dev/api/planets/1/'
print(get_residents_count(url))




