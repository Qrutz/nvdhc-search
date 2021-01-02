from tmdbv3api import TMDb, Movie, Authentication, Account
import fanks
from fanks import password, uname

USERNAME = uname
PASSWORD = password


tmdb = TMDb()
tmdb.api_key = '478b83570d49bc6dc32f339b9f0e06c4'
tmdb.language = 'en'
tmdb.debug = True


auth = Authentication(username=USERNAME, password=PASSWORD)

account = Account()
details = account.details()


print(details.username, details.id)


movie = Movie()

# recommendations = movie.recommendations(movie_id=336843)


# search = movie.search("Whiplash")

# for result in search:
#     print(result.id)
#     print(result.title)
#     print(result.overview)
#     print(result.poster_path)
#     print(result.vote_average)


# # for recommendation in recommendations:
# #     print(recommendation.title)
