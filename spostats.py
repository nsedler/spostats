# fuck you ill comment later

import spotipy
from dotenv import load_dotenv
import json
from spotipy.oauth2 import SpotifyOAuth

# results = sp.current_user_top_tracks()["items"]
# print(type(results))
# print(f'{results[0]["artists"][0]["name"]} - {results[0]["name"]} ({results[0]["album"]["name"]})')
# Directly from dictionary
# with open('json_data.json', 'w') as outfile:
#     json.dump(results, outfile)
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " - ", track['name'])cls


class Spostats():

    load_dotenv()

    def __init__(self):

        self.scopes = ["user-library-read", "user-read-playback-state"]

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scopes))
        

    def get_top_tracks(self, limit=25, offset=0, time_range="medium_term"):

        top_tracks = self.sp.current_user_top_tracks(
            limit=limit, offset=offset, time_range=time_range)['items']

        tracks = {}
        for idx, track in enumerate(top_tracks):

            artists = {'name': [], 'artist_page_link': []}

            album = {'name': track['album']['name'], 'album_page_link': track['album']['external_urls']['spotify'], 'album_cover_link': 
                track['album']['images'][0]['url'], 'release_date': track['album']['release_date']}

            song = {'name': track['name'], 'song_page_link': track['external_urls']
                    ['spotify'], 'duration': track['duration_ms']}

            for artist in track['artists']:
                artists['name'].append(artist['name'])
                artists['artist_page_link'].append(
                    artist['external_urls']['spotify'])

            track = {'artists': artists, 'album': album, 'song': song}
            tracks[idx] = track

        return tracks

    def get_top_artists(self, limit=25, offset=0, time_range="medium_term"):

        top_artists = self.sp.current_user_top_artists(
            limit=limit, offset=offset, time_range=time_range)['items']

        artists = {}
        for idx, artist in enumerate(top_artists):

            cur_artist = {'name': artist['name'], 'genres': [], 'artist_page_link': artist['external_urls']['spotify'], 'artist_image_link': artist['images'][0]['url']}

            for genre in artist['genres']:
                cur_artist['genres'].append(genre)

            artists[idx] = cur_artist

        return artists

    def get_playback_state(self):
        state = self.sp.current_playback()
        return state


spostat = Spostats()

spostat.get_playback_state()

print('gay')
