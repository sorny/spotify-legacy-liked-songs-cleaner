# spotify-legacy-liked-songs-cleaner
### Version 0.1

Clean up your liked songs playlist, back from the days where liking an album added all its songs to your liked songs... Was in back in 2015 :D?


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
5) Update liked-songs-cleaner.py with client id and client secret of your app
6) Run the script
```sh
python3 liked-songs-cleaner.py
```
7) Note, when running the script for the first time, your default browser will open and you will be redirected to authorize this script to modify your playlists etc. Good old Oauth2 magic (:


Have fun and use with care, its your precious liked songs you are dealing with.

License
----

MIT

**Free Software, Hell Yeah!**

