import datetime
import math
from time import sleep

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tqdm import trange, tqdm

# params
# for client id and secret, create a new application over at https://developer.spotify.com/dashboard
# when running this script for the first time, your browser will be redirected to grant authorization to this script
# to really delete the songs, set DRYRUN to False
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://localhost:8888/callback"
DRYRUN = False

# setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-library-read playlist-modify-private user-library-modify"))

# collect metainfo
saved_tracks_metainfo = sp.current_user_saved_tracks()
print("Total liked songs:", saved_tracks_metainfo['total'])

print("Collecting liked songs...")
query_offset = 50
saved_tracks = []
albums = {}
tracks = {}
tracks_to_delete = {}
albums_to_delete = {}
for i in trange(math.ceil(saved_tracks_metainfo['total'] / query_offset)):
    songs = sp.current_user_saved_tracks(query_offset, query_offset * i)
    saved_tracks.extend(songs['items'])

for item in saved_tracks:
    track = item['track']
    tracks[track['id']] = track
    albums[track['album']['id']] = track['album']

# check for albums whose tracks all are in users liked songs and mark them to delete
# also add the album to users favorites :)
print("Start scanning for whole albums in liked songs...")
sleep(0.5)
pbar = tqdm(albums.keys())
for album_id in pbar:
    pbar.set_description("Scanning " + album_id)
    album = sp.album(album_id)
    album_size = len(album['tracks']['items'])
    found_tracks_of_album = 0

    for track in album['tracks']['items']:
        if track['id'] in tracks.keys():
            found_tracks_of_album += 1

    # not gonna delete smaller albums, if you still want to, edit here
    if album_size == found_tracks_of_album & album_size > 2:
        albums_to_delete[album_id] = album

        # add the album to the saved albums if not already there
        if not sp.current_user_saved_albums_contains([album_id]):
            sp.current_user_saved_albums_add([album_id])
        for track in album['tracks']['items']:
            tracks_to_delete[track['id']] = track

# start deleting and log deleted track ids, also add tracks to a private spotify playlist
if len(tracks_to_delete) > 0:
    print("Marked albums to be deleted from liked songs:")
    for album_id, album in albums_to_delete.items():
        print(" ", album_id, "-", album["name"], "-", album['artists'][0]['name'])

    filename = "deleted_songs_" + datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')
    log_file = open(filename + ".log", "w")
    log_file.write("Deleted track ids:\n")

    print("Start deleting tracks from liked songs...")
    sleep(0.5)
    deleted_songs_playlist = sp.user_playlist_create(sp.current_user()['id'], filename, public=False,
                                                     collaborative=False,
                                                     description='Deleted songs from your liked songs')
    pbar = tqdm(tracks_to_delete.keys())
    for track_id in pbar:
        pbar.set_description("Deleting " + track_id)
        sp.playlist_add_items(deleted_songs_playlist['id'], [track_id])
        if DRYRUN:
            sleep(0.01)
        else:
            sp.current_user_saved_tracks_delete([track_id])
        log_file.write(track_id + "\n")

    print("Done, deleted tracks count:", len(tracks_to_delete))
    log_file.close()
else:
    print("Done, nothing to delete")
