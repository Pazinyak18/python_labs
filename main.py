from album_manager.album_manager import AlbumManager
from album.compact_cassette import CompactCassette
from album.laser_disc import LaserDisc
from album.vinyl_lp import VinylLp
from album.album import Gener


def main():
    manager = AlbumManager([
        CompactCassette("What's the Story Morning Glory?", "Oasis", Gener.Rock, 10, 100, 200, 20, True),
        LaserDisc("Le Dernier des heros", "KINO", Gener.Rock, 9, 300, 100, "Video-CD", 8589934592, 2),
        VinylLp("Imagine", "John Lennon", Gener.Rock, 10, 400, 300, 33, 5, 5)
    ])

    print("_______________________________________________________")
    print("Sorted by price in alphabetical order")
    # print("\n".join([str(a) for a in manager.sort_by_name(False)]))
    print(f"".join([str(a) for a in manager.sort_by_name(False)]))


if __name__ == '__main__':
    main()
