from album.album import Album
from album.laser_disc import LaserDisc
from album.album import Gener


class AlbumManager:
    def __init__(self, albums: list[Album] = None):
        self.albums = albums

    def search_song_for_cd(self, gener: Gener, duration_in_sec: int = 0):
        songs = []
        for song in self.albums:
            if isinstance(song, LaserDisc) and song.type_of_gener == gener and song.duration_in_sec < duration_in_sec:
                songs.append(song)
        return songs

    def sort_by_name(self, reverse: bool = False):
        return sorted(self.albums, key=lambda a: a.name, reverse=reverse)

    def sort_by_price(self, reverse: bool = False):
        return sorted(self.albums, key=lambda a: a.price, reverse=reverse)
