from django.test import TestCase


class LocalWeatherTestCase(TestCase):
    test_city = 'London'
    test_broken_city = 'Лондан'

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_weather(self):
        response = self.client.post(f'/get-weather/?city={self.test_city}')
        self.assertEqual(response.status_code, 200)

    def test_get_weather_broken(self):
        response = self.client.post(f'/get-weather/?city={self.test_broken_city}')
        self.assertEqual(response.status_code, 200)

    def test_cities_report(self):
        response = self.client.get('/cities-report/')
        self.assertEqual(response.json(), {})
