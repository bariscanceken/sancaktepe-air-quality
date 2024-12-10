#Library
import requests
import pandas as pd
import tkinter
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tabulate import tabulate
import os

#os
base_dir = os.path.dirname(os.path.abspath(__file__))
path_tabulate = os.path.join(base_dir, 'tabulates.txt')

#pull
url = "https://api.waqi.info/feed/sancaktepe/?token=2fad932ee24a2508b6e6c75d858a680e46b746f5"
response = requests.get(url).json()

#level
if response["data"]["aqi"] <= 50:
    l_aqi = "Good"
    x_aqi = 1
elif response["data"]["aqi"] <= 100:
    l_aqi = "Moderate"
    x_aqi = 2
elif response["data"]["aqi"] <= 150:
    l_aqi = "Unhealthy for Sensitive Groups"
    x_aqi = 3
elif response["data"]["aqi"] <= 200:
    l_aqi = "Unhealthy"
    x_aqi = 4
elif response["data"]["aqi"] <= 300:
    l_aqi = "Very Unhealthy"
    x_aqi = 5
elif response["data"]["aqi"] <= 500:
    l_aqi = "Hazardous"
    x_aqi = 6

if response["data"]["iaqi"]["co"]["v"] <= 4.4:
    l_co = "Good"
    x_co = 1
elif response["data"]["iaqi"]["co"]["v"] <= 9.4:
    l_co = "Moderate"
    x_co = 2
elif response["data"]["iaqi"]["co"]["v"] <= 12.4:
    l_co = "Unhealthy for Sensitive Groups"
    x_co = 3
elif response["data"]["iaqi"]["co"]["v"] <= 15.4:
    l_co = "Unhealthy"
    x_co = 4
elif response["data"]["iaqi"]["co"]["v"] <= 30.4:
    l_co = "Very Unhealthy"
    x_co = 5
elif response["data"]["iaqi"]["co"]["v"] <= 50:
    l_co = "Hazardous"
    x_co = 6

if response["data"]["iaqi"]["pm25"]["v"] <= 12:
    l_pm25 = "Good"
    x_pm25 = 1
elif response["data"]["iaqi"]["pm25"]["v"] <= 35.4:
    l_pm25 = "Moderate"
    x_pm25 = 2
elif response["data"]["iaqi"]["pm25"]["v"] <= 55.4:
    l_pm25 = "Unhealthy for Sensitive Groups"
    x_pm25 = 3
elif response["data"]["iaqi"]["pm25"]["v"] <= 150.4:
    l_pm25 = "Unhealthy"
    x_pm25 = 4
elif response["data"]["iaqi"]["pm25"]["v"] <= 250.4:
    l_pm25 = "Very Unhealthy"
    x_pm25 = 5
elif response["data"]["iaqi"]["pm25"]["v"] <= 500:
    l_pm25 = "Hazardous"
    x_pm25 = 6

if response["data"]["iaqi"]["pm10"]["v"] <= 54:
    l_pm10 = "Good"
    x_pm10 = 1
elif response["data"]["iaqi"]["pm10"]["v"] <= 154:
    l_pm10 = "Moderate"
    x_pm10 = 2
elif response["data"]["iaqi"]["pm10"]["v"] <= 254:
    l_pm10 = "Unhealthy for Sensitive Groups"
    x_pm10 = 3
elif response["data"]["iaqi"]["pm10"]["v"] <= 354:
    l_pm10 = "Unhealthy"
    x_pm10 = 4
elif response["data"]["iaqi"]["pm10"]["v"] <= 424:
    l_pm10 = "Very Unhealthy"
    x_pm10 = 5
elif response["data"]["iaqi"]["pm10"]["v"] <= 604:
    l_pm10 = "Hazardous"
    x_pm10 = 6

if response["data"]["iaqi"]["o3"]["v"] <= 54:
    l_o3 = "Good"
    x_o3 = 1
elif response["data"]["iaqi"]["o3"]["v"] <= 70:
    l_o3 = "Moderate"
    x_o3 = 2
elif response["data"]["iaqi"]["o3"]["v"] <= 85:
    l_o3 = "Unhealthy for Sensitive Groups"
    x_o3 = 3
elif response["data"]["iaqi"]["o3"]["v"] <= 105:
    l_o3 = "Unhealthy"
    x_o3 = 4
elif response["data"]["iaqi"]["o3"]["v"] <= 200:
    l_o3 = "Very Unhealthy"
    x_o3 = 5
elif response["data"]["iaqi"]["o3"]["v"] <= 400:
    l_o3 = "Hazardous"
    x_o3 = 6

if response["data"]["iaqi"]["no2"]["v"] <= 53:
    l_no2 = "Good"
    x_no2 = 1
elif response["data"]["iaqi"]["no2"]["v"] <= 100:
    l_no2 = "Moderate"
    x_no2 = 2
elif response["data"]["iaqi"]["no2"]["v"] <= 360:
    l_no2 = "Unhealthy for Sensitive Groups"
    x_no2 = 3
elif response["data"]["iaqi"]["no2"]["v"] <= 649:
    l_no2 = "Unhealthy"
    x_no2 = 4
elif response["data"]["iaqi"]["no2"]["v"] <= 1250:
    l_no2 = "Very Unhealthy"
    x_no2 = 5
elif response["data"]["iaqi"]["no2"]["v"] > 1250:
    l_no2 = "Hazardous"
    x_no2 = 6

if response["data"]["iaqi"]["so2"]["v"] <= 35:
    l_so2 = "Good"
    x_so2 = 1
elif response["data"]["iaqi"]["so2"]["v"] <= 75:
    l_so2 = "Moderate"
    x_so2 = 2
elif response["data"]["iaqi"]["so2"]["v"] <= 185:
    l_so2 = "Unhealthy for Sensitive Groups"
    x_so2 = 3
elif response["data"]["iaqi"]["so2"]["v"] <= 304:
    l_so2 = "Unhealthy"
    x_so2 = 4
elif response["data"]["iaqi"]["so2"]["v"] <= 605:
    l_so2 = "Very Unhealthy"
    x_so2 = 5
elif response["data"]["iaqi"]["so2"]["v"] > 605:
    l_so2 = "Hazardous"
    x_so2 = 6

veriable_values_level = [l_co,"%","°C",l_no2,l_o3,"Mb",l_pm10,l_pm25,l_so2,"C°","Km/H",l_aqi]

#Pandas
veriable_names = ["Carbon Monoxide ","Dew Point ","Humidity","Nitrogen Dioxide","Ozone","Pressure","Particulate Matter 10","Particulate Matter 2.5","Sulfur Dioxide","Temperature","Wind Speed","Air Quality Index"]
veriable_values = [response["data"]["iaqi"]["co"]["v"] , response["data"]["iaqi"]["dew"]["v"] , response["data"]["iaqi"]["h"]["v"] , response["data"]["iaqi"]["no2"]["v"] , response["data"]["iaqi"]["o3"]["v"] , response["data"]["iaqi"]["p"]["v"] , response["data"]["iaqi"]["pm10"]["v"] , response["data"]["iaqi"]["pm25"]["v"] , response["data"]["iaqi"]["so2"]["v"] , response["data"]["iaqi"]["t"]["v"] , response["data"]["iaqi"]["w"]["v"] , response["data"]["aqi"]]
trydataframe = pd.DataFrame(veriable_values , index = veriable_names , columns=["Value"])
trydataframe = trydataframe.rename_axis("Veriable")
trydataframe["Level"] = veriable_values_level

#Matplotlib
veriable_values_measurable  = x_aqi,x_co,x_pm25,x_pm10,x_o3,x_no2,x_so2
veriable_names_short =["aqi","co","pm25","pm10","o3","no2","so2"]
fig, ax = plt.subplots()
ax.bar(veriable_names_short , veriable_values_measurable)
plt.xlabel("VARIABLES")
plt.ylabel("DANGER LEVEL")
fig.set_figwidth(4)
fig.set_figheight(4)

def download_graphic():
    path_graph = os.path.join(base_dir,'Sancaktepe_AQI.png')
    fig.savefig(path_graph)

#Tabulate 
xtext = tabulate(trydataframe,headers="keys",tablefmt="simple")

def download_tabulate():
    with open(path_tabulate, 'a') as dosya:
        dosya.write(f"\n\n{xtext}\nDate the data was taken: {response["data"]["time"]["s"]}\n\n")

#Tkinter
window = tkinter.Tk()
window.title("Air Quality For Sancaktepe")
window.geometry("1000x480")
text_white = tkinter.Label(text=" ",background="White",height=1000,width=1000)
text_white.place(x=0,y=0)
text_welcome = tkinter.Label(text="Sancaktepe Air Quality",font="Arial 28",background="White")
text_welcome.place(x=0,y=20)
text_data = tkinter.Text(window, wrap=tkinter.WORD,height=15,)
text_data.pack(expand=True, fill="both")
text_data.insert(tkinter.END, xtext)
text_data.config(state=tkinter.DISABLED)
text_data.place(x=20,y=100)
button_download_graphic = tkinter.Button(text="Save Graphic",command=download_graphic)
button_download_graphic.place(x=730,y=440)
button_download_tabulate = tkinter.Button(text="Save Tabulate",command=download_tabulate)
button_download_tabulate.place(x=220,y=440)
canvas = FigureCanvasTkAgg(fig,master=window)
canvas.get_tk_widget().place(x=520,y=-60)
window.mainloop()