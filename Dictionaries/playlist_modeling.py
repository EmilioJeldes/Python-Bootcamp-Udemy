playlist = {
    "title": "patagonia bus",
    "author": "Colt Steele",
    "songs": [
        {"name": "Song_name", "author": "autor_name", "album": "album_name", "duration": 2.5},
        {"name": "Song_name", "author": "autor_name", "album": "album_name", "duration": 2.5},
        {"name": "Song_name", "author": "autor_name", "album": "album_name", "duration": 2.5},
        {"name": "Song_name", "author": "autor_name", "album": "album_name", "duration": 2.5},
        {"name": "Song_name", "author": "autor_name", "album": "album_name", "duration": 2.5},
        {"name": "Song_name", "author": "autor_name", "album": "album_name", "duration": 2.5},
        {"name": "Song_name", "author": "autor_name", "album": "album_name", "duration": 2.5}
    ]
}

total_duration = 0

for song in playlist["songs"]:
    total_duration += song["duration"]

print(total_duration)
