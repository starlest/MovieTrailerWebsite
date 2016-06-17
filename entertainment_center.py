import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

rocky = media.Movie("Rocky", "A small-time boxer rising to stardom.",
                    "https://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg",
                    "https://www.youtube.com/watch?v=7RYpJAUMo2M")

movies = [toy_story, avatar, rocky]
fresh_tomatoes.open_movies_page(movies)
