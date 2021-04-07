from .album import Album
from .album import Gener


class VinylLp(Album):
    def __init__(self, name: str = " ", band: str = " ", type_of_gener: Gener = 0, amount_of_songs: int = 0,
                 duration_in_sec: int = 0, price: float = 0, rpm: int = 0, amount_of_songs_on_side_a: int = 0,
                 amount_of_songs_on_side_b: int = 0):
        super().__init__(name, band, type_of_gener, amount_of_songs, duration_in_sec, price)
        self.rpm = rpm
        self.amount_of_songs_on_side_a = amount_of_songs_on_side_a
        self.amount_of_songs_on_side_b = amount_of_songs_on_side_b

    def __str__(self):
        return f"{super().__str__()}" \
               f"Rpm: {self.rpm}\n" \
               f"Amount of songs on side A: {self.amount_of_songs_on_side_a}\n" \
               f"Amount of songs on side B{self.amount_of_songs_on_side_b}\n"
