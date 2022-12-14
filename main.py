import time
import spotipy
import lyricsgenius as lg


cid = ''
secret = ''
uri = 'https://google.com'
genius_access_token = ''
scope = 'user-read-currently-playing'

oauth_object = spotipy.SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri=uri, scope=scope)

#spotify object
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotify_object = spotipy.Spotify(auth=token)


#genius object
genius_object = lg.Genius(genius_access_token)

current = spotify_object.currently_playing()


while True:
    current = spotify_object.currently_playing()
    status = current['currently_playing_type']

    if status == 'track':
        artist_name = current['item']['album']['artists'][0]['name']
        song_title = current['item']['name']

        length = current['item']['duration_ms']
        progress = current['progress_ms']
        time_left = int(((length-progress)/1000))

        song = genius_object.search_song(title=song_title, artist=artist_name)
        lyrics = song.lyrics
        print(lyrics)
        print("--------------------------------------------")

        time.sleep(time_left)

    elif status=='ad':
        time.sleep(30)
