function showWeather() {
        event.preventDefault();

        var city = document.getElementById('inputDefault').value;

        const weatherCard = document.getElementById('weatherCard');
        const weatherHeader = document.getElementById('weatherHeader');
        const weatherText = document.getElementById('weatherText');

        if (!city) {
            weatherCard.classList.add('alert', 'alert-dismissible', 'alert-warning');
            weatherHeader.textContent = 'Ошибка!';
            weatherText.textContent = 'Введите название города!';
            return;
        }

        weatherHeader.textContent = `Погода на сегодня в ${city}`;

        fetch(`http://127.0.0.1:8000/get-weather?city=${city}`)
            .then(response => {
                                weatherText.textContent = 'Получение информации...';
                                return response;
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    if (data.error == 'no_city') {
                        weatherCard.classList.add('alert', 'alert-dismissible', 'alert-warning');
                        weatherHeader.textContent = 'Ошибка!';
                        weatherText.textContent = 'Город не найден! Проверьте правильность названия.';
                    }
                    console.error('Произошла ошибка', data.error);
                } else {weatherText.innerHTML = data.weather}
            })
            .catch(error => console.error('Произошла ошибка', error));
    }