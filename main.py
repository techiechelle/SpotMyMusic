import SpotifyHelper
import YoutubeHelper

def main():
    playlistName = "New Year"
    SpotifyHelper.SpotifyClient()
    spotify_songs = SpotifyHelper.getCurrentUserPlaylists(playlistName)

    if spotify_songs is None:
        print(playlistName + " not found")
        return
    else:
        YoutubeHelper.createClient()
        return YoutubeHelper.startQuery(spotify_songs)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
Resources to review:
https://docs.python.org/3/tutorial/classes.html
https://docs.python.org/3/tutorial/inputoutput.html
https://cs50.harvard.edu/python/2022/weeks/8/
https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/

"""