import requests

resp = requests.post("https://predicttest-238017122334.us-central1.run.app", files={'file': open('C:/Users/Evonence/Desktop/Google-cloud-run/test/eight.png', 'rb')})

print(resp.json())
