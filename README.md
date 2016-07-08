# MovieWeb
# [Movie Web Generator]


Movie Web Generator is a Python based software that allow to the users to generate a web pages with predefined movie information such a title, trailer, main actors/actresses, and rating.

To get started, please execute the python file "entertainment_center.py" and a new generated web page will be opened in your default browser.

## Table of contents

* [Quick start](#quick-start)
* [Adding new movies](#adding_movies)
* [Versioning](#versioning)
* [Creators](#creators)
* [Copyright and license](#copyright-and-license)


## Quick start

* [Download the files: fresh_tomatoes.py, media.py, entertainment_center.py](https://github.com/carlesmb/MovieWeb.zip).
* Or clone the repo: `git clone https://github.com/carlesmb/MovieWeb.git`.
* Execute entertainment_center.py to generate the default web page

## adding_movies

The code generate a web page of movies based on the number of classes "Movie" instanciated on entertainment_center.py. To add a new Movie just add the following lines of code:

new_movie=media.Movie("trailer url", 
	"image url",
	 "title", "actors", "cinemas", 
	 "rating")

And after that, add your new movie in the List generated at the bottom of the file, before calling the function open_movies_page()

movies=[pi,braveheart,requiem_fa_dream, new_movie]


## Creators

**Carles Matamala**

* <https://twitter.com/carlesmb>
* <https://github.com/carlesmb>

based on the code leaarned in Udacity: nanodegree full-stack development

## Copyright and license

Code and documentation copyright 2016 Docs released under [GNU Creative Commons]

