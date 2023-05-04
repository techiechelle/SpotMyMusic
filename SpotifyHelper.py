import spotipy
from spotipy.oauth2 import SpotifyOAuth
import secrets

_scope = ""
_client = None

'''
    Initialize spotify OAuth client
'''
def createClient():
    _client = SpotifyOAuth(
        client_id=secrets.SPOTIPY_CLIENT_ID,
        client_secret=secrets.SPOTIPY_CLIENT_SECRET,
        redirect_uri=secrets.SPOTIPY_REDIRECT_URI,
        scope=_scope
    )

'''
    loop through the playlists and check if they match playlistName. If found, return the playlist's ID. Otherwise, return empty
'''

def getCurrentUserPlaylists(playlistName, limit = 100, offset=0):
    playlists = _client.get_current_user_playlists(limit=limit, offset=offset)

    if playlists.total < offset: return
    for playlist in playlists['items']:
        if playlistName is not None and playlistName == playlist['name']:
            return getSongsFromPlaylist(playlist['id'])
    getCurrentUserPlaylists(playlistName, limit, limit)

'''
    loop through the tracks in the specified playlist and return a list of songInfos (song name, artist name, album name)
'''

def getSongsFromPlaylist(playlistId):
    if playlistId is None: return
    tracksInfo = _client.playlist_tracks(playlist_id=playlistId, fields='total, items.track.name, items.track.artists.name, items.track.album.name')
    songs=tracksInfo.items
    offset = 0;
    tracksCount = len(tracksInfo.items.track)
    while tracksInfo.total > offset:
        offset += tracksCount
        tracksInfo = _client.playlist_tracks(playlist_id=playlistId, fields='total, items.track.name, items.track.artists.name, items.track.album.name', limit=tracksCount, offset=offset)
        songs = songs+tracksInfo.items
    formattedSongs = []
    for song in songs:
        formattedSongs += song.track
    return formattedSongs




