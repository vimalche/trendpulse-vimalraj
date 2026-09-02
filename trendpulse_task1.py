# -*- coding: utf-8 -*-
## fetch file from HackersNews

import requests
import json
import time

from datetime import datetime

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}

response = requests.get(url, headers=headers)

print(response.status_code)

story_ids = response.json()[:500]

print("Number of story IDs:", len(story_ids))
print("First 10 IDs:", story_ids[:10])

## get the details of each stories

headers = {"User-Agent": "TrendPulse/1.0"}
stories = []
for id in story_ids:
  url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    story = response.json()
    stories.append(story) # Append the story to the list
  else:
    print(f"Error: {response.status_code}")

print("Number of stories:", len(stories))
print("First 10 stories:", stories[:10])

## create a json file

import os

os.makedirs("data", exist_ok=True)

with open("data/trends_20240115.json", "w") as f:

  json.dump(stories, f)

  print("Data saved to data/trends_20240115.json")

  print("Number of stories:", len(stories))





