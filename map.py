import requests
import pandas as pd
import numpy as np


# importing geopy library
from geopy.geocoders import Nominatim

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# entering the location name
location=input("Enter location name:")

getLoc = loc.geocode(location)

# printing address
print(getLoc.address)

address=getLoc.address
latitude=getLoc.latitude
longitude= getLoc.longitude

# printing latitude and longitude
print("Latitude = ", latitude, "\n")
print("Longitude = ", longitude)



