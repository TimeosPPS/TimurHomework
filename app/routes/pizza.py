from flask import render_template
from app.db import Session, Pizza
from app import app
import requests

@app.get("/menu/")
def menu():
    city = "Київ"
    api_key = "df9ec52b25e6d249f02eb43a918de169"
    base_url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}"
    weather = requests.get(base_url)
    weather_data = weather.json()

    weather_main = weather_data["weather"][0]["main"]
    description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"] - 273.15

    session = Session()
    pizzas = session.query(Pizza).all()
    session.close()

    return render_template('menu.html', menu=pizzas, temperature=temperature, city=city, weather_main=weather_main, description=description)
@app.route('/main/')
def mainpage():
    city = "Київ"
    api_key = "df9ec52b25e6d249f02eb43a918de169"
    date = "1672531200"
    base_url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&dt={date}"
    weather = requests.get(base_url)
    weather_data = weather.json()

    weather_main = weather_data["weather"][0]["main"]
    description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"] - 273.15

    session = Session()
    pizzas = session.query(Pizza).all()
    if temperature < 0:
        pizza = session.query(Pizza).filter_by(id=4).all()
    elif 0 <= temperature <= 20:
        pizza = session.query(Pizza).filter_by(id=4).all()
    else:
        pizza = session.query(Pizza).filter_by(id=4).all()

    session.close()

    return render_template('index.html', city=city, date=date, weather_main=weather_main, description=description, temperature=temperature, pizza=pizza)

