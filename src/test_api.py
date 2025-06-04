import requests
API_KEY = 
response = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=SE&key={API_KEY}")
print(response.json())
