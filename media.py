import webbrowser
class Movie():
    """ This class represent Movie blueprint from which individual object create.
    """
    def __init__(self,movie_title,movie_storyline,poster_image,
               trailer_youtube):
        """This function create memory structure for Movie object and initalize 
        with information provided by callee.
        """
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    def show_trailer(self):
        """ This method open youtube link in a browser provided during initalization .
        """
        webbrowser.open(self.trailer_youtube_url)
