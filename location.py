from geopy.geocoders import Nominatim
import time
from pprint import pprint


# instantiate a new Nominatim client
app = Nominatim(user_agent="GetLocation")
# ask user to input desired location to get coordinates
desired_location = input("Which location do you want to get it's coordinates? ")
# get location raw data
location = app.geocode(desired_location).raw
# print raw data
pprint(location)
