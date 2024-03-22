from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '4aabafc87014ff23f087fc1c2776cf55'


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    if weather_data.get('cod') != 200:
        return 'Error: Unable to fetch weather data'

    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']

    return f'The weather in the city {city}: {temperature} C, with {weather_description}'


if __name__ == '__main__':
    app.run()

