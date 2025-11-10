import time
import csv
import os
import spotipy 
from spotipy.oauth2 import SpotifyOAuth

# Get track information from Spotify Web API
def retrieve_track_data(client_id, client_secret, redirect_uri, batch):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri))
    track_list = sp.tracks(batch)
    for track in track_list['tracks']:
        print(track['name'], track['artists'][0]['name'])

# Create time delay between retrieving batches
def time_delay():
    time.sleep(1)


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
def consume_batches(batch):
    path = "track_list.csv"
    if os.path.isfile(path):
        with open("track_list.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([id])
    else:
        with open("track_list.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([id])
            print("CSV file created")

def run_exporter(client_id, client_secret):
    if os.path.exists("track_list.csv"):
        os.remove("track_list.csv")
    full_links = read_links("Full_Links.txt")
    cleaned = clean_links(full_links)
    parsed_ids = extract_ids(cleaned)
    batches = get_batches(parsed_ids)
    for batch in batches:
        retrieve_track_data(client_id, client_secret, batch)
        consume_batches(batch)

if __name__ == "__main__":
    run_exporter(client_id="CLIENTid", client_secret="CLIENTsecret", redirect_uri="http://127.0.0.1:8000/callback")