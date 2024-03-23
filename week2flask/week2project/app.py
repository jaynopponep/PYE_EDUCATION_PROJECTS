from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '[INSERT YOUR API KEY HERE]'


def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial'
    response = requests.get(url)
    weather_data = response.json()

    if weather_data.get('cod') != 200:
        return None, 'Error: Unable to fetch weather data for ' + city

    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']
    return f'{temperature} F, with {weather_description}'


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    city1 = request.form['city1']
    city2 = request.form['city2']

    weather1 = get_weather(city1)
    weather2 = get_weather(city2)

    return f'The weather in {city1}: {weather1}<br>The weather in {city2}: {weather2}'


if __name__ == '__main__':
    app.run()
