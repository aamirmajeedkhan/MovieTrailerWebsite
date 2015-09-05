import fresh_tomatoes
from media import Movie
""" This module create instance of Movie class and use module fresh_tomatoes to display in browser.
"""

#Initialize Movie Object with title,youtube url, poster etc.
toy_story = Movie("Toy Story","A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

beautiful_mind= Movie("A Beautiful Mind","""A biographical drama film based on the life of John Nash, 
                         a Nobel Laureate in Economics.""",
                     "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                     "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

theory_of_Everthing= Movie("The Theory of Everything","""A film adapted from the memoir Travelling to Infinity:
                         My Life with Stephen by Jane Wilde Hawking, which deals with her relationship with 
                         her ex-husband, theoretical physicist Stephen Hawking, his diagnosis of motor neuron 
                         disease, and his success in physics. drama film based on the life of John Nash, a 
                         Nobel Laureate in Economics.""",
                     "https://upload.wikimedia.org/wikipedia/en/b/b8/Theory_of_Everything.jpg",
                     "https://www.youtube.com/watch?v=LUayjO_KgsQ")

little_boy= Movie("Little Boy","""The story centers on a 7-year-old boy, Pepper Flynt Busbee (Jakob Salvati),
                   who is devastated when his father enlists in the army during World War II.""",
                     "https://upload.wikimedia.org/wikipedia/en/a/a2/Little_Boy_poster.jpg",
                     "https://www.youtube.com/watch?v=b_BdzqsIX6A")

amerian_history= Movie("American History X","""The film tells the story of two Venice, Los Angeles brothers who
                        become involved in the neo-Nazi movement. The older brother serves three years in prison
                        for voluntary manslaughter, changes his beliefs and tries to prevent his brother from 
                        going down the same path.""",
                     "https://upload.wikimedia.org/wikipedia/en/0/0a/American_history_x_poster.jpg",
                     "https://www.youtube.com/watch?v=JsPW6Fj3BUI")

great_debaters= Movie("The Great Debaters","""TBased on a true story, the plot revolves around the efforts of
                      debate coach Melvin B. Tolson (Denzel Washington) at historically black Wiley College to 
                      place his team on equal footing with whites in the American South during the 1930s.""",
                     "https://upload.wikimedia.org/wikipedia/en/f/f5/Great_debaters_post.jpg",
                     "https://www.youtube.com/watch?v=IN2AGZThL-8")

movies = [toy_story,beautiful_mind,theory_of_Everthing,little_boy,amerian_history,great_debaters]
#Module fresh tomatoes display movie array in a web browser 
fresh_tomatoes.open_movies_page(movies)


