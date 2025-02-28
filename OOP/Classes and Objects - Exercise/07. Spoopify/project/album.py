from project.song import Song
from typing import Optional, List


class Album:
    def __init__(self, name: str, song: Optional[Song] = None):
        self.name = name
        self.song = song
        self.published: bool = False
        self.songs: list = []

    def add_song(self, song: Song) -> str:
        if self.song:
            self.songs.append(self.song)
        if song in self.songs:
            return "Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."
        song = next((s for s in self.songs if s.name == song_name), None)
        if song is None:
            return "Song is not in the album."
        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return (f'Album {self.name}\n'
                + "\n".join([f" == {song.get_info()}" for song in self.songs])
                + "\n")
