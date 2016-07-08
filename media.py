#We will create a Parent class Video with the basic information that Video can contain

class Video():
	def __init__(self, trailer_youtube_url, poster_image_url, title, actors):
		self.trailer_youtube_url=trailer_youtube_url
		self.poster_image_url=poster_image_url
		self.title=title
		self.actors=actors

#After creating the Parent class, we create two Childs (Movie and Serie) that will inherit all the
#Parent information plus we will add an specific info

class Movie(Video):
	def __init__(self, trailer_youtube_url, poster_image_url, title, actors, cinemas, imdt_rating):
		Video.__init__(self, trailer_youtube_url, poster_image_url, title, actors)
		self.cinemas=cinemas
		self.imdt_rating=imdt_rating

class Serie(Video):
	def __init_(self, trailer_youtube_url, poster_image_url, title, actors, season):
		Video.__init__(self, trailer_youtube_url, poster_image_url, title, actors)
		self.season=season