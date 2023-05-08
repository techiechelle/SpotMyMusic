# SpotMyMusic
This is a simple app to check if song in my Spotify playlist exists in youtube.

---
Build Instructions:<br>
Install Spotipy<br>
`pip install spotipy --upgrade`

Create .secrets.py in the root folder. This file contains your redirect URL, spotify client ID and secret. This file ***should not*** be committed to git.
This file should look like the following
```
SPOTIPY_CLIENT_ID=''
SPOTIPY_CLIENT_SECRET=''
SPOTIPY_REDIRECT_URI=''
```