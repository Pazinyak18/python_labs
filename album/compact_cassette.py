from .album import Album
from .album import Gener


class CompactCassette(Album):
    def __init__(self, name: str = " ", band: str = " ", type_of_gener: Gener = 0, amount_of_songs: int = 0,
                 duration_in_sec: int = 0, price: float = 0, capasity_in_sec: int = 0, two_sides: bool = False):
        super().__init__(name, band, type_of_gener, amount_of_songs, duration_in_sec, price)
        self.capasity_in_sec = capasity_in_sec
        self.two_sides = two_sides

    def __str__(self):
        return f"{super().__str__()}" \
               f"Capacity in sec: {self.capasity_in_sec}\n" \
               f"Two sides: {self.two_sides}\n"
