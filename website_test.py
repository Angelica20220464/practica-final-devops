import requests

def website_test():
    url = 'http://localhost:8000'
    response = requests.get(url)
    assert response.status_code == 200
    assert '<h1>Hola Mundo mi nombre es angelica:)</h1>' in response.text