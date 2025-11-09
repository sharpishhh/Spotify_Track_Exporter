import time
from itertools import zip_longest

with open("Full_Links.txt", "r") as file:
    full_links = file.readlines()

def extract_ids():
    result = []
    for track in full_links:
        result.append(track.removeprefix("https://open.spotify.com/track/").rstrip())
    return result

def get_batches(arr):
    length = len(arr)
    for i in range(0,length-1,6):
        yield arr[i, i+6]
  

    

        

if __name__ == "__main__":
    # print(extract_ids())
    # print(get_batches())
    # print(grouper(iterable=[1,2,3,4,5,5,6,7,8,8,9,9,9,6,5,4,3],num=5, incomplete='fill', fillvalue=None))
    print(get_batches([1,2,3,4,5,5,6,7,8,8,9]))
