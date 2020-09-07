from dataclasses import dataclass


class Vessel:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)
