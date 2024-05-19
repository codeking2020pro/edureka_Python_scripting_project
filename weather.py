# A Weather App using API
from tkinter import *
import requests
import json
from _datetime import datetime
from PIL import ImageTk, Image

# WINDOW SETUP
window = Tk()
window.title("Weather App")
window.geometry("500x740")
window['background'] = "white"

# DEVELOPER'S PICTURE
new = ImageTk.PhotoImage(Image.open('Roland.png'))
panel = Label(window, image=new)
panel.place(x=425, y=620)

# DATE ITEMS
dt = datetime.now()
day = Label(window, text=dt.strftime('%A--'), bg='white', font=("bold", 14))
day.place(x=5, y=130)
month = Label(window, text=dt.strftime('%d %B'), bg='white', font=("bold", 14))
month.place(x=100, y=130)
year = Label(window, text=dt.year, bg='white', font=("bold", 14))
year.place(x=170, y=130)

# TIME ITEMS
item = Label(window, text='Time--', bg='white', font=("bold", 14))
item.place(x=5, y=160)
time = Label(window, text=dt.strftime('%H : %M : %S'), bg='white', font=("bold", 14))
time.place(x=100, y=160)

# DAY & NIGHT THEME INDICATORS
if int((dt.strftime('%H'))) >= 6 & int((dt.strftime('%H'))) <= 18:
	img = ImageTk.PhotoImage(Image.open('sun.jpg'))
	panel = Label(window, image=img)
	panel.place(x=400, y=100)
else:
	img = ImageTk.PhotoImage(Image.open('moon.jpg'))
	panel = Label(window, image=img)
	panel.place(x=400, y=100)

# City Search
city_name = StringVar()
city_entry = Entry(window, textvariable=city_name, width=45)
city_entry.grid(row=1, column=0, ipady=15, stick=W+E+N+S)


def city_name():

	# API Call
	api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
					+ city_entry.get() + "&units=metric&appid="+'366c5efbe472e3d631b1bc12d0bc379d')
	api = json.loads(api_request.content)

	# Weather Conditions
	y = api['main']
	current_temperature = y['temp']
	humidity = y['humidity']
	temp_min = y['temp_min']
	temp_max = y['temp_max']

	# Coordinates
	x = api['coord']
	longitude = x['lon']
	latitude = x['lat']

	# Country
	z = api['sys']
	country = z['country']
	citi = api['name']

	# Adding the received info into the screen
	label_temp.configure(text=current_temperature)
	label_humidity.configure(text=humidity)
	max_temp.configure(text=temp_max)
	min_temp.configure(text=temp_min)
	label_lon.configure(text=longitude)
	label_lat.configure(text=latitude)
	label_country.configure(text=country)
	label_citi.configure(text=citi)


# WINDOW FORMATTING - SEARCH BAR AND BUTTON
city_nameButton = Button(window, text="Search", command=city_name)
city_nameButton.grid(row=1, column=1, padx=10, stick=W+E+N+S)


# WINDOW FORMATTING - CITY, COUNTRY & COORDINATES
label_citi = Label(window, text="...", width=0, bg='white', font=("bold", 14))
label_citi.place(x=10, y=63)

label_country = Label(window, text="...", width=0, bg='white', font=("bold", 14))
label_country.place(x=135, y=63)

item = Label(window, text='Long.:', bg='white', font=("bold", 14))
item.place(x=5, y=95)
item = Label(window, text='Lat.:', bg='white', font=("bold", 14))
item.place(x=145, y=95)
label_lon = Label(window, text="...", width=0, bg='white', font=("Helvetica", 14))
label_lon.place(x=65, y=95)
label_lat = Label(window, text="...", width=0, bg='white', font=("Helvetica", 14))
label_lat.place(x=185, y=95)

# WINDOW FORMATTING - CURRENT TEMPERATURE
item = Label(window, text='Current Temperature:', bg='white', font=("bold", 18))
item.place(x=5, y=210)
label_temp = Label(window, text="...", width=0, bg='white', font=("Helvetica", 32), fg='black')
label_temp.place(x=90, y=250)

# WINDOW FORMATTING - RELATED WEATHER INFO
humid = Label(window, text="Humidity: ", width=0, bg='white', font=("bold", 12))
humid.place(x=3, y=400)
label_humidity = Label(window, text="...", width=0, bg='white', font=("bold", 12))
label_humidity.place(x=107, y=400)

# WINDOW FORMATTING - MAXIMUM & MINIMUM TEMPERATURE
maxi = Label(window, text="Max. Temp.: ", width=0, bg='white', font=("bold", 12))
maxi.place(x=3, y=430)
max_temp = Label(window, text="...", width=0, bg='white', font=("bold", 12))
max_temp.place(x=107, y=430)

mini = Label(window, text="Min. Temp.: ", width=0, bg='white', font=("bold", 12))
mini.place(x=3, y=460)
min_temp = Label(window, text="...", width=0, bg='white', font=("bold", 12))
min_temp.place(x=107, y=460)

# WINDOW FORMATTING - FOOTNOTE
footnote = Label(window, text="All temperatures in degree celsius", bg='white', font=("italic", 10))
footnote.place(x=5, y=665)


window.mainloop()
