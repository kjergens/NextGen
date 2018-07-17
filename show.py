from datetime import datetime


class Show:
    """
    A class to represent a Netflix show or movie.
    """

    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year

    def __repr__(self):
        s = "{0} ({1}) - {2} - {3} years ago"
        return s.format(self.title, self.year, self.genre, (datetime.now().year - self.year))
