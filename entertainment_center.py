import fresh_tomatoes
import media

lego_movie = media.Movie("Lego Movie",
                        "Legos come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg",
                        "https://www.youtube.com/watch?v=fZ_JOBCLF-I")
#print(toy_story.storyline)

incredibles = media.Movie("The Incredibles 2",
                     "The superhero family is back!",
                     "https://upload.wikimedia.org/wikipedia/en/2/27/The_Incredibles_2.jpg",
                     "https://www.youtube.com/watch?v=i5qOzqD9Rms")
#print(avatar.storyline)

spongebob = media.Movie("The SpongeBob SquarePants Movie",
                     "A Sponge on the Big Screen",
                     "https://upload.wikimedia.org/wikipedia/en/3/31/The_SpongeBob_SquarePants_Movie_poster.jpg",
                     "https://www.youtube.com/watch?v=EVhpSZK5KuY")

alien = media.Movie("Alien",
                     "In space, no one can hear you scream",
                     "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
                     "https://www.youtube.com/watch?v=LjLamj-b0I8")

neighbor = media.Movie("Wont You Be My Neighbor",
                     "Documentary on Mr. Rogers",
                     "https://upload.wikimedia.org/wikipedia/en/7/7d/Won%27t_You_Be_My_Neighbor%3F.png",
                     "https://www.youtube.com/watch?v=FhwktRDG_aQ")

panda = media.Movie("Kung Fu Panda",
                     "The chosen one fights!",
                     "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
                     "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

movies = [lego_movie,incredibles,spongebob,alien,neighbor,panda]
fresh_tomatoes.open_movies_page(movies)
