from spotipy.oauth2 import SpotifyOAuth
import spotipy
from os import getenv, path, remove

class Spotify:
    def __init__(self) -> None:
        self.SpotifyAuth = SpotifyOAuth(client_id=getenv("SPOTIFY_CLIENT_ID"), client_secret=getenv("SPOTIFY_CLIENT_SECRET"), scope=getenv("SPOTIFY_SCOPE"), redirect_uri=getenv("SPOTIFY_REDIRECT_URI"))
        self.Spotify = spotipy.Spotify(auth_manager=self.SpotifyAuth)

    def clear_token(self) -> None:
        if (path.exists(".cache")):
            remove(".cache")

    def get_all_playlist(self):
        # self.clear_token()
        self.allplaylist = self.Spotify.current_user_playlists()
        return self.allplaylist
