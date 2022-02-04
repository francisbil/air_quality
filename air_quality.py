from tkinter import *
import requests
import json

api_key = ''

def enter_zipcode():
    global info
    x = entry.get()
    entry.delete(0, END)
    url = 'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + str(x) + '&distance=0&API_KEY=' + api_key

    try:
        api_request = requests.get(url)
        api_response = json.loads(api_request.content)
        city = api_response[0]['ReportingArea']
        value = str(api_response[0]['AQI'])
        category = api_response[0]['Category']['Name']
        string = city + ', ' + value + ', ' + category
        color = colors[category]
    except Exception as e:
        api_response = "Error..."

    info['text'] = string

root = Tk()
root.title('Weather App')

colors = {'Good': '#00E400', 'Moderate': 'yellow', 'Unhealthy for Sensitive Groups': '#00E400', 'Unhealthy': 'red', 'Very Unhealthy': '#00E400', 'Hazardous': '#7E0023'}

try:
    api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=60007&distance=0&API_KEY=' + api_key)
    api_response = json.loads(api_request.content)
    city = api_response[0]['ReportingArea']
    value = str(api_response[0]['AQI'])
    category = api_response[0]['Category']['Name']
    string = city + ', ' + value + ', ' + category
    color = colors[category]
except Exception as e:
    api_response = "Error..."

root.configure(background=color)
info = Label(root, text=string, background=color, font=('Helvetica', 20))
info.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

label = Label(root, text='Zipcode')
label.grid(row=1, column=0)

entry = Entry(root, width=20)
entry.grid(row=1, column=1)

button = Button(root, text='Enter', command=enter_zipcode)
button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
