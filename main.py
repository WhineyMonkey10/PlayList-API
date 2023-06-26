import fastapi
import requests
import os
import dotenv
import random
import json

dotenv.load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")

app = fastapi.FastAPI()

# Use Genius API to get a random song
@app.get("/random_song/{playListLength}")
def randomSong(playListLength: int):
    songList = []
    for i in range(playListLength):
        songID = random.randint(1, 9195000)
        headers = {'Authorization': f'Bearer {access_token}'}
        url = f"https://api.genius.com/songs/{songID}"
        response = requests.get(url, headers=headers).json()

        try:
            title = response["response"]["song"]["title"]
            artist = response["response"]["song"]["primary_artist"]["name"]
            song = {"title": title, "artist": artist}
            songList.append(song)
        except KeyError:
            print(f"Error: Unable to retrieve song information for ID {songID}.")
            continue

    # Return the song list as a JSON response
    return songList
