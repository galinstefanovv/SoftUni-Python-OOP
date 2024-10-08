from typing import List

from album import Album


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'

        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        try:
            check_album = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f'Album {album_name} is not found.'

        if check_album.published:
            return f'Album has been published. It cannot be removed.'

        self.albums.remove(check_album)
        return f'Album {album_name} has been removed.'

    def details(self):
        return f"Band {self.name}\n" \
               f"{Album.details}"


