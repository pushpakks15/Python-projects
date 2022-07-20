import requests
from bs4 import BeautifulSoup


ID="6fb13552af534c3db5d9f383d51aa248"
Secret="0fd67c6be4bd4a84945c430e388c6916"
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=ID,
        client_secret=Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

year=input("Which year do you want to travel to?")
response=requests.get(f"https://www.lyricsia.com/hindi-songs/{year}")
data=response.text
soup=BeautifulSoup(data,"html.parser")
songs=soup.find_all(name="a")
list_of_songs=[song.getText() for song in songs][3:100]
song_uris = []
for song in list_of_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Songs", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)



