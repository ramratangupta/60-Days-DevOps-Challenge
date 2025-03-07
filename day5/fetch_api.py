import requests
try:
    data = requests.get("https://jsonplaceholder.typicode.com/users")
    if data.status_code==200:
        apiData = data.json()
        for row in apiData:
            print(f"{row['id']}\t{row['name']}")
except Exception as e:
    print(e)
