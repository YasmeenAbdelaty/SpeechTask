import requests
api_address="https://newsapi.org/v2/everything?q=tesla&from=2022-11-15&sortBy=publishedAt&apiKey=7da9924c8935449f98b9809d7c1b79b1"
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):
        ar.append(", "+ json_data["articles"][i]["title"]+ ".")

        return ar


