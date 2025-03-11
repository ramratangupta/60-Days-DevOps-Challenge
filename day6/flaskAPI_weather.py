from flask import Flask
app = Flask(__name__)
import requests

@app.route("/")
def home():
    data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    return data.content
if __name__ == "__main__":
    app.run("127.0.0.1",3000,True)