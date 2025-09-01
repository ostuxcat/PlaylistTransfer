from Modules.SpotifyController import Spotify
from Modules.YoutubeController import YoutubeMusic
from dotenv import load_dotenv

def main():
    load_dotenv()
    sp = Spotify()
    yt = YoutubeMusic()
    sp.get_all_playlist()
    for playlist in sp.allplaylist["items"]:
        allSongs:list = []
        playlist_uri = playlist["uri"].split(":")[2]
        yt_playlist = yt.createPlaylist(playlist["name"])
        print(f"[{playlist["name"]}]")
        for track in sp.Spotify.playlist_items(playlist_uri)["items"]:
            trackName: str = track["track"]["name"]
            artistNames: str = ""
            for artist in track["track"]["artists"]:
                if artistNames == "":
                    artistNames = f"{artistNames} {artist["name"]}"
                    continue
                artistNames = f"{artistNames}, {artist["name"]}"
            finalSearchString: str = f"{artistNames} - {trackName}"
            if finalSearchString not in yt.AllSongsData.keys():
                result = yt.search_song(finalSearchString)
                if(len(result)):
                    yt.AllSongsData[finalSearchString] = result[0]["videoId"]
                    allSongs.append(result[0]["videoId"])
            else:
                result = yt.AllSongsData[finalSearchString]
                allSongs.append(result)
            print(finalSearchString)
        added_to_playlist_songs = yt.add_to_playlist(yt_playlist, allSongs)
        print(f"Added {added_to_playlist_songs}\n")
if __name__ == "__main__":
    main()
