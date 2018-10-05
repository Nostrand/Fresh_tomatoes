import media
import fresh_tomatoes

scott = media.Movie("Scott Pilgrim vs The World", "Scott Pilgrim must defeat his new girlfriend's seven evil exes in order to win her heart.",
	"https://m.media-amazon.com/images/M/MV5BMTkwNTczNTMyOF5BMl5BanBnXkFtZTcwNzUxOTUyMw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
	"https://www.youtube.com/watch?v=7wd5KEaOtm4")

terra = media.Movie("Battle for Terra", "The last hope for an alien race.",
	"https://upload.wikimedia.org/wikipedia/en/thumb/e/e2/Battle-for-terra-poster.jpg/220px-Battle-for-terra-poster.jpg",
	"https://www.youtube.com/watch?v=wYfB-Npq_IA")

men = media.Movie("Man in Black", "A police officer joins a secret organization that polices and monitors extraterrestrial interactions on Earth.",
	"https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Men_in_Black_Poster.jpg/220px-Men_in_Black_Poster.jpg",
	"https://www.youtube.com/watch?v=HYUd7AOw_lk")

matrix = media.Movie("The Matrix", "The search for the truth.",
	"https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
	"https://www.youtube.com/watch?v=vKQi3bBA1y8")

chris = media.Movie("The Pursuit of Happyness", "A struggling salesman and his son, go on a life-changing path.",
	"https://upload.wikimedia.org/wikipedia/en/thumb/8/81/Poster-pursuithappyness.jpg/220px-Poster-pursuithappyness.jpg",
	"https://www.youtube.com/watch?v=89Kq8SDyvfg")

walterm = media.Movie("The Secret life of Walter Mitty", "A global journey that turns into an adventure more extraordinary than anything you could have ever imagined",
	"https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Secret_Life_of_Walter_Mitty_poster.jpg/220px-The_Secret_Life_of_Walter_Mitty_poster.jpg",
	"https://www.youtube.com/watch?v=QD6cy4PBQPI")

movies = [scott, terra, men, matrix, chris, walterm]
fresh_tomatoes.open_movies_page(movies)

'''
Alternate way to run the movie instances
def run():
    """ Generate and open the movies listing html page """
    fresh_tomatoes.open_movies_page(
            get_movie_list())


def get_movie_list():
    """ Retrieve a list of movies """
    return [media.Movie("Scott Pilgrim vs The World", "Scott Pilgrim must defeat his new girlfriend's seven evil exes in order to win her heart.",
	"https://m.media-amazon.com/images/M/MV5BMTkwNTczNTMyOF5BMl5BanBnXkFtZTcwNzUxOTUyMw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
	"https://www.youtube.com/watch?v=7wd5KEaOtm4"),
	media.Movie("Battle for Terra", "The last hope for an alien race.",
	"https://upload.wikimedia.org/wikipedia/en/thumb/e/e2/Battle-for-terra-poster.jpg/220px-Battle-for-terra-poster.jpg",
	"https://www.youtube.com/watch?v=wYfB-Npq_IA"),
	media.Movie("Man in Black", "A police officer joins a secret organization that polices and monitors extraterrestrial interactions on Earth.",
	"https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Men_in_Black_Poster.jpg/220px-Men_in_Black_Poster.jpg",
	"https://www.youtube.com/watch?v=HYUd7AOw_lk"),
	media.Movie("The Matrix", "The search for the truth.",
	"https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
	"https://www.youtube.com/watch?v=vKQi3bBA1y8"),
	media.Movie("The Secret life of Walter Mitty", "A global journey that turns into an adventure more extraordinary than anything you could have ever imagined",
	"https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Secret_Life_of_Walter_Mitty_poster.jpg/220px-The_Secret_Life_of_Walter_Mitty_poster.jpg",
	"https://www.youtube.com/watch?v=QD6cy4PBQPI"),
	media.Movie("The Pursuit of Happyness", "A struggling salesman and his son, go on a life-changing path.",
	"https://upload.wikimedia.org/wikipedia/en/thumb/8/81/Poster-pursuithappyness.jpg/220px-Poster-pursuithappyness.jpg",
	"https://www.youtube.com/watch?v=89Kq8SDyvfg")]

run()
'''