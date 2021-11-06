import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

load_dotenv()

SPOTIFY_SEARCH_LINK = "https://api.spotify.com/v1/search"
SPOTIFY_PUBLIC = os.getenv("SPOTIFY_PUBLIC")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")

def spotify_credential_manager():
    client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_PUBLIC, client_secret=SPOTIFY_SECRET) 
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_for_artist(artist):
    spotify = spotify_credential_manager()
    spotify_artist_https = spotify.search(artist)['tracks']['items'][0]['album']['artists'][0]['external_urls']['spotify']
    spotify_artist_api = spotify.search(artist)['tracks']['items'][0]['album']['artists'][0]["href"]
    print(spotify_artist_https)
    print(spotify_artist_api)

search_for_artist("Muse")

