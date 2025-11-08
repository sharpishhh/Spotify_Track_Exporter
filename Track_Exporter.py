import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Open the file of full track links
with open("Full_Links.txt", "r") as file:
    full_links = file.readlines()

def extract_track_id(full_links):
    result = []
    for link in full_links:
        result.append(link.removeprefix("https://open.spotify.com/track/").rstrip())
    return result


def retrieve_tracks():
    auth_manager = SpotifyClientCredentials(client_id='', client_secret='')
    sp = spotipy.Spotify(auth_manager=auth_manager)
    track_list = extract_track_id(full_links)
    final_list = sp.tracks(track_list)
    print(final_list['name'] + '-' + final_list['artists'][0]['name'])

if __name__ == "__main__":
    print(retrieve_tracks())


'''   def get_args():
    parser = argparse.Argu mentParser(description='Print artist and track name given a list of track IDs')
    parser.add_argument('-u', '--uris', nargs='+', required=True, help='Track ids')
    return parser.parse_args()'''