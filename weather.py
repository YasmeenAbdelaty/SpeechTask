import requests
api_address='http://api.openweathermap.org/data/2.5/weather?q=cairo&appid=41a5754cd15f2c44a97c33df9dba193c'
json_data=requests.get(api_address).json()


def temp():
    temprature= round(json_data["main"]["temp"]-273,1)
    return temprature

def des():
    description=json_data["weather"][0]["description"]
    return description

