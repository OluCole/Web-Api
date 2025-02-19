import os
import requests
from io import BytesIO
# API Endpoint

import requests 
from PIL import Image 

api_key = os.environ['Nasa_api_key']

def astronauts_in_space():
  url = "http://api.open-notify.org/astros.json"



  
  #send request and parse response as JSON
  response =  requests.get(url)
  print(response)
  data = response.json()
  
  #Print number of astronauts in space
  print(data["Number of astronauhts in space:", data]["number"])
  
  #Print names of austronauts 
  # print(f"{person['name']} is on the craft (person['craft].")


def nasa_pic_of_day(api_key):
  url = url = "https://api.nasa.gov/planetary/apod"
  date = "2015-05-05"
  params = {"api_key": api_key, "date": date, "hd": "True"}

  response = requests.get(url, params=params)
  print(response)
  data = response.json()
  print(data)
  if response.status_code == 200 and data["media_type"] == "image" and "hdurl" in data:
  #print(image.content)
    image = requests.get(data[0]["hdurl"])
    img = Image.open(BytesIO(image.content))
    title = data["title"]
    img.save(f"./images/{title}.jpg")

# def get_dog_pic():
#   url = "https://api.thedogapi.com/v1/images/search"
#   result = requests.get(url)
#   data = result.json()
#   print("data")
#   image = requests.get(data["url"])
#   img = Image.open(BytesIO(image.content))
#   title = "Random DOg Pick"
#   img.save(f"./images/{title}.jpg")

def get_philosopher_info():
  url = "https://philosophyapi.pythonanywhere.com/api/ideas/"
  response = requests.get(url)
  print(response)
  data = response.json()
  print(data["results"][0]["author"])
  print(data["results"][0]["quote"])
  print()
  print()

def get_philosophers_info():
  topic = input("Enter topic: ")
  url = f"http://philosophyapi.pythonanywhere.com/api/ideas/?search={topic}"
  response = requests.get(url)
  print(response)
  data = response.json()
  for i in range(len(data)-1):
    print(data["results"][i]["author"])
    print(data["results"][i]["quote"])

  
  


#   #Get umsge URL data
#   image_url = data["url"]
#   print("NASA's Picture of the Day:", image_url)

get_philosopher_info()
get_philosophers_info()
# get_dog_pic()
# nasa_pic_of_day(api_key)
