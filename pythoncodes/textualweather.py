import requests
from textual.app import App
from textual.containers import Container
from textual.widgets import Header, Footer, Button, Label, Input, Static

class WeatherInfo(Static):
    def __init__(self, city, weather_data, **kwargs):
        super().__init__(**kwargs)
        self.city = city
        self.weather_data = weather_data
        self.label = Label(self.format_weather_data())
        self.refresh_button = Button("Refresh", id="refresh-button")
        self.compose()

    def compose(self):
        self.update(Container(self.label, self.refresh_button, id="weather-container"))

    def format_weather_data(self):
        temp = self.weather_data["main"]["temp"]
        description = self.weather_data["weather"][0]["description"]
        humidity = self.weather_data["main"]["humidity"]
        wind_speed = self.weather_data["wind"]["speed"]
        return f"Weather in {self.city}:\nTemperature: {temp}°C\nCondition: {description.capitalize()}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"

    def refresh(self):
        self.label.update(self.format_weather_data())

    def on_button_pressed(self, event):
        button = event.sender
        if button.id == "refresh-button":
            self.refresh()

class WeatherApp(App):
    CSS_PATH = "weather.css"

    def compose(self):
        yield Header()
        yield Footer()
        self.city_input = Input(placeholder="Enter city name", id="city-input")
        self.search_button = Button("Search", id="search-button")
        self.weather_display = Container(id="weather-display")
        yield Container(self.city_input, self.search_button, id="input-container")
        yield self.weather_display

    def fetch_weather(self, city):
        api_key = "your_openweather_api_key"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def on_button_pressed(self, event):
        button = event.sender
        if button.id == "search-button":
            city = self.city_input.value.strip()
            if city:
                weather_data = self.fetch_weather(city)
                if weather_data:
                    weather_info = WeatherInfo(city, weather_data)
                    self.weather_display.clear()
                    self.weather_display.mount(weather_info)
                else:
                    self.weather_display.clear()
                    self.weather_display.mount(Label(f"Could not retrieve weather data for {city}."))
            self.city_input.update("")

if __name__ == "__main__":
    WeatherApp().run()
