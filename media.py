import webbrowser


class Movie():
    """
    Movie class that has title, storyline, poster image,
    and a url to its trailer.
    
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image_url, trailer_youtube):
        """
        Constructor takes parameters as strings
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        open the trailer_youtube_url link
        in the default browser
        """
        webbrowser.open(self.trailer_youtube_url)
