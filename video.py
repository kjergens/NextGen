from datetime import datetime


class Video:
    """
    A class to represent a Netflix show or movie.
    """
    title = ""
    genre = ""
    year = 0

    def __repr__(self):
        s = "{0} ({1}) - {2} - {3} years ago"
        return s.format(self.title, self.year, self.genre, (datetime.now().year - self.year))
