import media
import fresh_tomatoes

# After importing the necessary classes from media and 
# fresh_tomatoes, we instanciate 3 objects of Movie

pi=media.Movie("https://www.youtube.com/watch?v=oQ1sZSCz47w", 
	"http://www.newschool.edu/uploadedImages/Divisional_Events/NSGS/pi.jpg",
	 "Pi", " Sean Gullette, Mark Margolis", "All-Stars cinema", 
	 "7.5/10")

braveheart=media.Movie("https://www.youtube.com/watch?v=j53_WxqPZ7c", 
	"http://4.bp.blogspot.com/-r7NCtJedhfo/UKK5idsWuUI/AAAAAAAAQ3E/QVBgy3QpLYU/s1600/Braveheart-movie-1.jpeg",
	 "Braveheart", "Mel Gibson, Sophie Marceau", "All-Stars cinema", 
	 "8/10")

requiem_fa_dream=media.Movie("https://www.youtube.com/watch?v=lgo3Hb5vWLE", 
	"http://www.blogcdn.com/blog.moviefone.com/media/2010/05/requiemforadream052810.jpg",
	 "Requiem for a dream", "Jennifer Connelly, Jared Leto", "All-Stars cinema", 
	 "8/10")

# After instanciate 3 objects of Movie, we create a list of 
# the Movie objects that we want to use in our webpage 

movies=[pi,braveheart,requiem_fa_dream]

# After creation the necessary list that fresh_tomatoes 
# expect, we send that list to the constructor of the webpage
fresh_tomatoes.open_movies_page(movies)