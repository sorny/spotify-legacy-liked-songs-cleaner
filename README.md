# spotify-legacy-liked-songs-cleaner
### Version 0.1

Clean up your liked songs playlist, back from the days where liking an album added all its songs to your liked songs... 
Was it back in 2015 :D? Anyway, this script is here to help. 


# Main Features:

  - Scans through your liked songs playlist. If a whole album is in there, this script will remove those songs.
  - Deleted songs will be savely moved to a new, dedicated Spotify playlist in your Spotify account so nothing is lost. 
  - Deleted song ids will be logged to a dedicated logfile. 
  - Also, fancy progress bars based on tqdm :)


### Tech

spotify-legacy-liked-songs-cleaner uses open source libs and open data to work properly:

* [Spotify Web API](https://developer.spotify.com/) - Spotify's Web API <3
* [Spotipy](https://github.com/plamere/spotipy) - A light weight Python library for the Spotify Web API
* [tqdm](https://github.com/tqdm/tqdm) - A Fast, Extensible Progress Bar for Python and CLI


# Installation
1) Clone this repo
2) Goto https://developer.spotify.com/dashboard/, sign in using your Spotify account and create a new app and note down client id and client secret
3) Install the requirements for this script
```sh
pip3 install -r requirements.txt
```
5) Update `liked_songs_cleaner.py` with client id and client secret of your app
6) Run the script in dryrun mode
```sh
python3 liked_songs_cleaner.py
```
7) If you are happy with the outcome of the deleted songs playlist, change `DRYRUN` to `False` in `liked_songs_cleaner.py` and rerun the script to free your liked songs from its legacy


### Notes

 * When running the script for the first time, your default browser will open and you will be redirected to authorize this script to modify your playlists. Good old Oauth2 magic (:
 * Required authorization scopes of this script: `user-library-read`, `playlist-modify-private`, `user-library-modify`
 * For details on the scopes, hit up https://developer.spotify.com/documentation/general/guides/scopes/



Have fun and use with care, its your precious liked songs you are dealing with.

License
----

MIT

**Free Software, Hell Yeah!**

