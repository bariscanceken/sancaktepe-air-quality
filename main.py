#Library
import requests

#pull
url = "https://api.waqi.info/feed/sancaktepe/?token=2fad932ee24a2508b6e6c75d858a680e46b746f5"
response = requests.get(url).json()
print(response)


