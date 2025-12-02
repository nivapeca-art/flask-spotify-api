from flask import Flask
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app=Flask(__name__)

CLIENT_ID = "6d4f4a619dac4c7d9f474585d64781e9"
CLIENT_SECRET = "51a259fc98d243b5816b6bcd57f3bd9c"

auth_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

sp = spotipy.Spotify(auth_manager=auth_manager)

@app.route('/songs')
def home():
    # Prueba: buscar 3 canciones de Shakira
    results = sp.search(q="Shakira", type="track", limit=3)
    tracks = [t["name"] for t in results["tracks"]["items"]]
    return f"Canciones encontradas: {tracks}"

if __name__ == '__main__':
    app.run(debug=True)