from ytmusicapi import YTMusic, OAuthCredentials
from os import getenv
class YoutubeMusic:
    def __init__(self):
        self.AllSongsData = {}
        self.Youtube = YTMusic(auth="oauth.json", oauth_credentials=OAuthCredentials(client_id=getenv("YOUTUBE_CLIENT_ID"), client_secret=getenv("YOUTUBE_CLIENT_SECRET")))
    def get_all_playlist(self):
        return self.Youtube.get_library_playlists(None)
    def createPlaylist(self, name, force=False):
        if not force:
            for playlist in self.get_all_playlist():
                if playlist["title"]==name:
                    return playlist["playlistId"]
        return self.Youtube.create_playlist(title=name, description=name)
    def search_song(self, name):
        return self.Youtube.search(query=name, filter="songs", limit=1)
    def add_to_playlist(self, playlist, allSongs):
        self.FilteredSongs = [[]]
        fetch_playlist = self.Youtube.get_playlist(playlist)
        if(len(fetch_playlist)):
            count=0
            idx=0
            for song in allSongs:
                isDuplicate = False
                for track in fetch_playlist["tracks"]:
                    if song == track["videoId"]:
                        isDuplicate = True
                        break
                if not isDuplicate:
                    if count >= 90:
                        idx = idx+1
                        count = 0
                    if (len(self.FilteredSongs)-1)<idx:
                        self.FilteredSongs.append([])
                    self.FilteredSongs[idx].append(song)
                    count = count+1
        if len(self.FilteredSongs[0]):
            for i in range(len(self.FilteredSongs)):
                try:
                    print(f"Total Songs: {len(self.FilteredSongs[i])}.")
                    return self.Youtube.add_playlist_items(playlist, self.FilteredSongs[i])
                except Exception as e:
                    print(e)
