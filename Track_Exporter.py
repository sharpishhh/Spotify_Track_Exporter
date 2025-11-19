import time
import csv
import os
import io
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()
print("starting track exporter.py")




def authorization(client_id, client_secret, redirect_uri, scope):
    # Use keyword arguments so SpotifyOAuth gets the right values
    auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp

# Get track information from Spotify Web API
def retrieve_track_data(sp, batch, current_row):
    track_info = {}
    trk_info_list = []
    track_list = sp.tracks(batch)
    for i, track in enumerate(track_list['tracks']):
        row_num = current_row + i
        artists = []
        for artist in track['artists']:
            artists.append(artist['name'])
        song_artists = ','.join(artists)
        track_info = {'Track ID': row_num, 'Song': track['name'], 'Artist(s)': song_artists}
        trk_info_list.append(track_info)
    
    return trk_info_list

# Create time delay between retrieving batches
def time_delay(sleep):
    return time.sleep(sleep)


# Open file and read in links
def read_links(file_path):
    with open(file_path, "r") as file:
       return file.readlines()

# Clean extra space from end of the links
def clean_links(full_links):
    cleaned = []
    for link in full_links:
        cleaned.append(link.rstrip())
    return cleaned

# Using the cleaned links, parse and extract the track IDs
def extract_ids(cleaned):
    parsed_ids = []
    for link in cleaned:
        parsed_ids.append(link.removeprefix("https://open.spotify.com/track/").rstrip())
    return parsed_ids

# Generate batches of digestable size to give to Spotify
def get_batches(parsed_ids):
    length = len(parsed_ids)
    for i in range(0,length,50):
        yield parsed_ids[i:i+50]

# Convert batches to CSV file.
# Use to create CSV file upon completion of parsing and batching.
def consume_batches(track_dict):
    path = "track_list.csv"
    fieldnames = ['Track ID', 'Song', 'Artist(s)']
    if os.path.isfile(path):
        with io.open("track_list.csv", "a",encoding='utf8', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for song in track_dict:
                writer.writerow(song)
    else:
        with io.open("track_list.csv", "w", encoding='utf8', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for song in track_dict:
                writer.writerow(song)
            print("CSV file created")

def run_exporter(client_id, client_secret, redirect_uri, scope):
    # Get a Spotify client instance
    sp = authorization(client_id, client_secret, redirect_uri, scope)
    print("Got Spotify client")

    # Start fresh each run
    if os.path.exists("track_list.csv"):
        print("Removing existing track_list.csv")
        os.remove("track_list.csv")
    current_row = 0
    full_links = read_links("Full_Links.txt")
    cleaned = clean_links(full_links)
    parsed_ids = extract_ids(cleaned)
    batches = get_batches(parsed_ids)
    
    batch_count = 0
    for batch in batches:
        batch_count += 1
        track_info = retrieve_track_data(sp, batch, current_row)
        consume_batches(track_info)
        current_row += len(batch)
        time_delay(.25)
    print(f"Created {batch_count} batches total")
    
if __name__ == "__main__":
    run_exporter(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET"), redirect_uri=os.getenv("REDIRECT_URI"), scope='user-library-read playlist-read-private')
 