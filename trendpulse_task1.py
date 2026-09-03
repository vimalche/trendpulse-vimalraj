# -*- coding: utf-8 -*-
## fetch file from HackersNews

import requests
import json
import time

from datetime import datetime, timezone

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}

response = requests.get(url, headers=headers)

print(response.status_code)

story_ids = response.json()[:500]

print("Number of story IDs:", len(story_ids))
print("First 10 IDs:", story_ids[:10])

## get the details of each stories

import os

def get_category(title):
  title_lower = title.lower()
  if any(word in title_lower for word in ['ai','gpt''llm','model','machine learing']):
    return "AI"
  elif any(word in title_lower for word in ['python','code','software','web','app','github']):
    return "TECH"
  elif any(word in title_lower for word in['startup','business','market','money','pay']):
    return "BUSINESS"
  elif any(word in title_lower for word in['science','physics','space','biology','math','research']):
    return "SCIENCE"
  else:
    return "OTHER"

headers = {"User-Agent": "TrendPulse/1.0"}
stories = []
for id in story_ids[:125]:
  url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    story = response.json()
    if story and story.get("type") == 'story' and 'title' in story:
      extracted_story = {"post_id" : story.get("id"),
                         "title" : story.get("title"),
                         "category" : story.get("title",""),
                         "score" : story.get("score",0),
                         "num_comments" : story.get("descendants",0),
                         "author" : story.get("by"),
                         "collected at" : datetime.now(timezone.utc).strftime("%Y-%m-%d %H-%M-%S")
                         }
    stories.append(story) 

  else:
    print(f"Error: {response.status_code}")

print("Number of stories:", len(stories))
print("First 10 stories:", stories[:1])

## create a json file

os.makedirs("data", exist_ok=True)

with open("data/trends_20240115.json", "w") as f:

  json.dump(stories, f)

  print("Data saved to data/trends_20240115.json")

  print("Number of stories:", len(stories))





