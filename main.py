#Library
import requests
import pandas as pd

#pull
url = "https://api.waqi.info/feed/sancaktepe/?token=2fad932ee24a2508b6e6c75d858a680e46b746f5"
response = requests.get(url).json()

#variables
veriable_names = ["Carbon Monoxide ","Dew Point ","Humidity","Nitrogen Dioxide","Ozone","Pressure","Particulate Matter 10","Particulate Matter 2.5","Sulfur Dioxide","Temperature","Wind Speed","Air Quality Index"]
veriable_values = [response["data"]["iaqi"]["co"]["v"] , response["data"]["iaqi"]["dew"]["v"] , response["data"]["iaqi"]["h"]["v"] , response["data"]["iaqi"]["no2"]["v"] , response["data"]["iaqi"]["o3"]["v"] , response["data"]["iaqi"]["p"]["v"] , response["data"]["iaqi"]["pm10"]["v"] , response["data"]["iaqi"]["pm25"]["v"] , response["data"]["iaqi"]["so2"]["v"] , response["data"]["iaqi"]["t"]["v"] , response["data"]["iaqi"]["w"]["v"] , response["data"]["aqi"]]

#level

if response["data"]["aqi"] <= 50:
    l_aqi = "Good"
elif response["data"]["aqi"] <= 100:
    l_aqi = "Moderate"
elif response["data"]["aqi"] <= 150:
    l_aqi = "Unhealthy for Sensitive Groups"
elif response["data"]["aqi"] <= 200:
    l_aqi = "Unhealthy"
elif response["data"]["aqi"] <= 300:
    l_aqi = "Very Unhealthy"
elif response["data"]["aqi"] <= 500:
    l_aqi = "Hazardous"

if response["data"]["iaqi"]["co"]["v"] <= 4.4:
    l_co = "Good"
elif response["data"]["iaqi"]["co"]["v"] <= 9.4:
    l_co = "Moderate"
elif response["data"]["iaqi"]["co"]["v"] <= 12.4:
    l_co = "Unhealthy for Sensitive Groups"
elif response["data"]["iaqi"]["co"]["v"] <= 15.4:
    l_co = "Unhealthy"
elif response["data"]["iaqi"]["co"]["v"] <= 30.4:
    l_co = "Very Unhealthy"
elif response["data"]["iaqi"]["co"]["v"] <= 50:
    l_co = "Hazardous"

if response["data"]["iaqi"]["pm25"]["v"] <= 12:
    l_pm25 = "Good"
elif response["data"]["iaqi"]["pm25"]["v"] <= 35.4:
    l_pm25 = "Moderate"
elif response["data"]["iaqi"]["pm25"]["v"] <= 55.4:
    l_pm25 = "Unhealthy for Sensitive Groups"
elif response["data"]["iaqi"]["pm25"]["v"] <= 150.4:
    l_pm25 = "Unhealthy"
elif response["data"]["iaqi"]["pm25"]["v"] <= 250.4:
    l_pm25 = "Very Unhealthy"
elif response["data"]["iaqi"]["pm25"]["v"] <= 500:
    l_pm25 = "Hazardous"

if response["data"]["iaqi"]["pm10"]["v"] <= 54:
    l_pm10 = "Good"
elif response["data"]["iaqi"]["pm10"]["v"] <= 154:
    l_pm10 = "Moderate"
elif response["data"]["iaqi"]["pm10"]["v"] <= 254:
    l_pm10 = "Unhealthy for Sensitive Groups"
elif response["data"]["iaqi"]["pm10"]["v"] <= 354:
    l_pm10 = "Unhealthy"
elif response["data"]["iaqi"]["pm10"]["v"] <= 424:
    l_pm10 = "Very Unhealthy"
elif response["data"]["iaqi"]["pm10"]["v"] <= 604:
    l_pm10 = "Hazardous"

if response["data"]["iaqi"]["o3"]["v"] <= 54:
    l_o3 = "Good"
elif response["data"]["iaqi"]["o3"]["v"] <= 70:
    l_o3 = "Moderate"
elif response["data"]["iaqi"]["o3"]["v"] <= 85:
    l_o3 = "Unhealthy for Sensitive Groups"
elif response["data"]["iaqi"]["o3"]["v"] <= 105:
    l_o3 = "Unhealthy"
elif response["data"]["iaqi"]["o3"]["v"] <= 200:
    l_o3 = "Very Unhealthy"
elif response["data"]["iaqi"]["o3"]["v"] <= 400:
    l_o3 = "Hazardous"

if response["data"]["iaqi"]["no2"]["v"] <= 53:
    l_no2 = "Good"
elif response["data"]["iaqi"]["no2"]["v"] <= 100:
    l_no2 = "Moderate"
elif response["data"]["iaqi"]["no2"]["v"] <= 360:
    l_no2 = "Unhealthy for Sensitive Groups"
elif response["data"]["iaqi"]["no2"]["v"] <= 649:
    l_no2 = "Unhealthy"
elif response["data"]["iaqi"]["no2"]["v"] <= 1250:
    l_no2 = "Very Unhealthy"
elif response["data"]["iaqi"]["no2"]["v"] > 1250:
    l_no2 = "Hazardous"

if response["data"]["iaqi"]["so2"]["v"] <= 35:
    l_so2 = "Good"
elif response["data"]["iaqi"]["so2"]["v"] <= 75:
    l_so2 = "Moderate"
elif response["data"]["iaqi"]["so2"]["v"] <= 185:
    l_so2 = "Unhealthy for Sensitive Groups"
elif response["data"]["iaqi"]["so2"]["v"] <= 304:
    l_so2 = "Unhealthy"
elif response["data"]["iaqi"]["so2"]["v"] <= 605:
    l_so2 = "Very Unhealthy"
elif response["data"]["iaqi"]["so2"]["v"] > 605:
    l_so2 = "Hazardous"

veriable_values_level = [l_co,"%","°C",l_no2,l_o3,"Mb",l_pm10,l_pm25,l_so2,"C°","Km/H",l_aqi]

#Pandas
trydataframe = pd.DataFrame(veriable_values , index = veriable_names , columns=["Value Today"])
trydataframe = trydataframe.rename_axis("Veriable")
trydataframe["Level"] = veriable_values_level


print(trydataframe)