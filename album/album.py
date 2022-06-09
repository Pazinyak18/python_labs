from enum import Enum


class Gener(Enum):
    Rock = 0
    Rap = 1
    Pop = 2


class Album:
    def __init__(self, name: str = " ", band: str = " ", type_of_gener: Gener = 0, amount_of_songs: int = 0,
                 duration_in_sec: int = 0, price: float = 0):
        self.name = name
        self.band = band
        self.type_of_gener = type_of_gener
        self.amount_of_songs = amount_of_songs
        self.duration_in_sec = duration_in_sec
        self.price = price

    def __str__(self):
        return f"Name: {self.name}\n " \
               f"Band:{self.band}\n " \
               f"Gener: {self.type_of_gener}\n " \
               f"Amount of songs: {self.amount_of_songs}\n " \
               f"Duration: {self.duration_in_sec}\n " \
               f"Price: {self.price}\n"
