import requests 
from datetime import datetime

# response=requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code!=200:
# #     raise Exception("bad response from ISS API")
# # if response.status_code==404:
# #     raise Exception("That response does not exist.")
# # elif response.status_code==401:
# #     raise Exception("you are not authorised to access this data.")
# response.raise_for_status()
# data=response.json()
# longitude=data['iss_position']['longitude']
# longitude=data['iss_position']['latitude']
# iss_position=(longitude,longitude)
# print(iss_position)

paramater={
    "lat":28.704060,
    "lng":77.102493,
    "ormatted":0
}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=paramater)
response.raise_for_status()
data=response.json()
sunrise=data['results']['sunrise'].split(":")[0]
sunset=data['results']['sunset'].split(":")[0]
print(sunrise)
print(sunset)

time_now=datetime.now()
print(time_now.hour)