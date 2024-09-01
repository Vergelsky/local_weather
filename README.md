
# # local_weather
### Простой сайт для просмотра погоды
С историей поиска, статистикой и подсказками

## Порядок установки:
###### (подразумевается что у вас уже установлен python, git, и docker)
- клонируем репозиторий:<br>
git clone https://github.com/Vergelsky/local_weather.git<br>

- создаём виртуальное окружение:<br>
python -m venv .venv
- активируем его:<br>
  .venv/Scripts/activate
- устанавливаем зависимости:<br>
pip install -r requirements.txt
- из файла env_example создаём файл с переменными окружения .env:<br>
copy env_expample .env<br>
и заполняем его своими значениями (WEATHER_API_KEY берем с https://www.weatherapi.com/)
- запускаем докер:<br>
docker-compose up --build

## Что удалось сделать <br>
- написаны тесты
- всё помещено в докер контейнер
- сделаны автодополнение (подсказки) при вводе города
- при повторном посещении сайта будет предложено посмотреть погоду в городе, в котором пользователь уже смотрел ранее
- для каждого пользователя сохраняется его история поиска. API для просмотра статистики поисков.
- (API доступно по адресу /cities-report/)

посмотреть рабочую версию можно по адресу https://weather.yasdelyal.ru/
