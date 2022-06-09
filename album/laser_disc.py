from .album import Album
from .album import Gener


class LaserDisc(Album):
    def __init__(self, name: str = " ", band: str = " ", type_of_gener: Gener = 0, amount_of_songs: int = 0,
                 duration_in_sec: int = 0, price: float = 0, cd_format: str = " ", amount_of_data_in_bits: int = 0,
                 amount_of_layers: int = 0):
        super().__init__(name, band, type_of_gener, amount_of_songs, duration_in_sec, price)
        self.cd_format = cd_format
        self.amount_of_data_in_bits = amount_of_data_in_bits
        self.amount_of_layers = amount_of_layers

    def __str__(self):
        return f"{super().__str__()}" \
               f"Format: {self.cd_format}\n" \
               f"Amount of data in bits: {self.amount_of_data_in_bits}\n" \
               f"Amount of layers {self.amount_of_layers}\n"
