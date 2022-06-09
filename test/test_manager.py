import unittest
from album_manager.album_manager import AlbumManager
from album.compact_cassette import CompactCassette
from album.laser_disc import LaserDisc
from album.vinyl_lp import VinylLp
from album.album import Gener


class TestManager(unittest.TestCase):
    manager = AlbumManager([
        CompactCassette("What's the Story Morning Glory?", "Oasis", Gener.Rock, 10, 100, 200, 20, True),
        LaserDisc("Le Dernier des heros", "KINO", Gener.Rock, 9, 200, 100, "Video-CD", 8589934592, 2),
        VinylLp("Imagine", "John Lennon", Gener.Rock, 10, 400, 300, 33, 5, 5)
    ])

    def test_sort_by_name_increase(self):
        for i in range(0, len(self.manager.albums)):
            for y in range(i+1, len(self.manager.albums)):
                if self.manager.albums[y].name > self.manager.albums[i].name:
                    temp = self.manager.albums[y]
                    self.manager.albums[y] = self.manager.albums[i]
                    self.manager.albums[i] = temp

        self.assertListEqual(self.manager.albums, self.manager.sort_by_name(True))

        # self.assertEqual(sorted(self.manager.albums, key=lambda a: a.name, reverse=True),
        #                 self.manager.sort_by_name(True))

    def test_sort_by_name_decrease(self):
        for i in range(0, len(self.manager.albums)):
            for y in range(i+1, len(self.manager.albums)):
                if self.manager.albums[y].name < self.manager.albums[i].name:
                    temp = self.manager.albums[y]
                    self.manager.albums[y] = self.manager.albums[i]
                    self.manager.albums[i] = temp

        self.assertListEqual(self.manager.albums, self.manager.sort_by_name(False))

        # self.assertEqual(sorted(self.manager.albums, key=lambda a: a.name, reverse=False),
        #                 self.manager.sort_by_name(False))

    def test_sort_by_price_increase(self):
        for i in range(0, len(self.manager.albums)):
            for y in range(i+1, len(self.manager.albums)):
                if self.manager.albums[y].price > self.manager.albums[i].price:
                    temp = self.manager.albums[y]
                    self.manager.albums[y] = self.manager.albums[i]
                    self.manager.albums[i] = temp

        self.assertListEqual(self.manager.albums, self.manager.sort_by_price(True))

        # self.assertEqual(sorted(self.manager.albums, key=lambda a: a.price, reverse=True),
        #                 self.manager.sort_by_price(True))

    def test_sort_by_price_decrease(self):
        for i in range(0, len(self.manager.albums)):
            for y in range(i+1, len(self.manager.albums)):
                if self.manager.albums[y].price < self.manager.albums[i].price:
                    temp = self.manager.albums[y]
                    self.manager.albums[y] = self.manager.albums[i]
                    self.manager.albums[i] = temp

        self.assertListEqual(self.manager.albums, self.manager.sort_by_price(False))

        # self.assertEqual(sorted(self.manager.albums, key=lambda a: a.price, reverse=False),
        #                 self.manager.sort_by_price(False))

    def test_search_song_for_cd(self):
        self.assertEqual(sorted(filter(
            lambda a: isinstance(a, LaserDisc) and a.type_of_gener == Gener.Rock and a.duration_in_sec < 300,
            self.manager.albums), key=lambda a: isinstance(a, LaserDisc)),
            self.manager.search_song_for_cd(Gener.Rock, 300))
