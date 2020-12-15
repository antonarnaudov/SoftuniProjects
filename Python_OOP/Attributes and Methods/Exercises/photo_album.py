class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                for x in range(len(self.photos[i])):
                    if self.photos[i][x] == label:
                        return f"{label} photo added " \
                               f"successfully on page {i + 1} slot {x + 1}"
        return "No more free spots"

    def display(self):
        result = ''
        for photos in self.photos:
            result += f"{'-' * 11}\n{' '.join([str([]) for x in photos])}\n{'-' * 11}\n"
        return result

# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())

album = PhotoAlbum(3)
print(album.add_photo("asdf"))
print(album.display())
