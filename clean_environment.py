import requests

try:
    print(requests.get("http://127.0.0.1:5000/stop_server"))
except Exception as e:
    print("An error occurred:", e)
finally:
    print('Server stopped')

try:
    requests.get("http://127.0.0.1:5001/stop_server")
except Exception as e:
    print("An error occurred:", e)
finally:
    print('Server stopped')
