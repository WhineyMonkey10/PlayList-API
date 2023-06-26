import fastapi
import requests
import os
import dotenv
import random

dotenv.load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
access_token = os.getenv("ACCESS_TOKEN")

app = fastapi.FastAPI()

# Use Genius api to get a random song

@app.get("/random_song/{playListLength}")
def randomSong(playListLength: int):
    songList = []
    for i in range(playListLength):
        songID = random.randint(1, 9195000)
        headers = {'Authorization': f'Bearer {access_token}'}
        url = f"https://api.genius.com/songs/{songID}"
        songList.append(requests.get(url, headers=headers).json()["response"]["song"]["title"] + " by " + requests.get(url, headers=headers).json()["response"]["song"]["primary_artist"]["name"])
    # Correctly format the song list
    for i in range(len(songList)):
        songList[i] = str(i + 1) + ". " + songList[i] + "\n"
    songList = "".join(songList)
    return songList

