python3 -m venv venv
. venv/bin/activate
pip install -r requirement.txt

* **Challenge 1**: Create a Python script that connects to a remote server via SSH using paramiko.
```
I tried with AmazonQ
but I am confident, will see soultion.
```
* **Challenge 2**: Build a simple Flask API with an endpoint that returns system health (CPU/memory usage).
python3 -m venv venv
. venv/bin/activate
pip install -r requirement.txt
code app_server_cpu_mem.py

```
from flask import Flask
import psutil
app = Flask(__name__)

@app.route("/")
def home():
    status = {}
    status["cpu_used"] = psutil.cpu_percent()
    status["ram_used"] = psutil.virtual_memory()[2]
    return status
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8081,debug=True)
```
python app_server_cpu_mem.py
open http://127.0.0.1:8081/
{
  "cpu_used": 20.1,
  "ram_used": 80.1
}

* **Challenge 3**: Create a Django app, set up models, views, and templates for a basic CRUD operation.
mkdir django_app
cd django_app
python3 -m venv venv
. venv/bin/activate
pip install Django
django-admin startproject curd_server
python manage.py runserver
python manage.py startapp myapp
* **Challenge 4**: Use python subprocess to execute system commands and capture output.
```
import subprocess
result = subprocess.run(["ls","-l"],capture_output=True,text=True)
print("STDOUT",result.stdout)
print("STDERROR",result.stderr)
print("STDREDURNOCDE",result.returncode)

```
* **Challenge 5**: Build a Flask API that fetches live weather data from an external API and returns it in JSON format.
code flaskAPI_weather.py
```
from flask import Flask
app = Flask(__name__)
import requests

@app.route("/")
def home():
    data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    return data.content
if __name__ == "__main__":
    app.run("127.0.0.1",3000,True)

```
. venv/bin/activate 
python flaskAPI_weather.py
open http://localhost:3000/

