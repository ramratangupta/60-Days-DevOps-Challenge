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