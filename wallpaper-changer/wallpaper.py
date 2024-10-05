import requests as req
from dotenv import dotenv_values
import random 
import ctypes

api_key = dotenv_values(".env")["KEY"]

# allow user to choose picture theme
theme = input("Enter picture theme: ")
# choose a random page from the url 
page_number = random.randint(1, 10)
# number of images returned 
IMAGES_PER_PAGE = 20
# random img number
img_number = random.randint(0, IMAGES_PER_PAGE - 1)

# url headers
headers = {
    "Authorization": api_key,
}

parameters = {
    "query": theme,
    "page": page_number,
    "per_page": IMAGES_PER_PAGE,
}

# pexels api url 
url = "https://api.pexels.com/v1/search"

# send api request for img
response = req.get(url, headers=headers, params=parameters)
# convert to json
data = response.json()

# parse the url for the img we want
img_url = data["photos"][img_number]["src"]["large2x"]

# split the img url 
img_url_split = img_url.split("/")

# extract img name 
img_name = img_url_split[5].split("?")[0]

# send a request to the url of the img 
img = req.get(img_url, stream=True)

# save the img to the imgs/
with open(f"img/{img_name}", "wb") as fd:
    for chunk in img.iter_content(chunk_size=128):
        fd.write(chunk)

# set the path to the wallpaper image
wallpaper_path = fr"E:\Python\practice-projects\wallpaper-changer\img\{img_name}"

# set the style of the wallpaper
# 0: Center, 1: Stretch, 2: Tile, 6: Fit
wallpaper_style = 6

# load the image
SPI_SETDESKWALLPAPER = 20
image = ctypes.c_wchar_p(wallpaper_path)

# set the wallpaper
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, wallpaper_style)
