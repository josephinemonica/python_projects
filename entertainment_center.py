import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=ZZv1vki4ou4")

avatar=media.Movie("Avatar", "A marine on an alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://youtu.be/5PSNL1qE6VY")  

me_before_you=media.Movie("Me Before You","A romantic drama film adapted from Jojo Moyes' novel of the same name", "https://upload.wikimedia.org/wikipedia/en/f/fd/Me_Before_You_%28film%29.jpg", "https://youtu.be/BUbCupJWFSE")

coco=media.Movie("Coco","A 12-year-old boy named Miguel Rivera who is accidentally transported to the land of the dead", "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg","https://www.youtube.com/watch?v=Ga6RYejo6Hk")

frozen=media.Movie("Frozen","A fearless princess who sets off on a journey to find her estranged sister, whose icy powers have inadvertently trapped their kingdom in eternal winter","https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg","https://www.youtube.com/watch?v=TbQm5doF_Uc")

gifted=media.Movie("Gifted","An intellectually gifted 7-year-old who becomes the subject of a custody battle between her uncle and grandmother","https://upload.wikimedia.org/wikipedia/en/f/fe/Gifted_film_poster.jpg","https://www.youtube.com/watch?v=TbQm5doF_Uc")

#movies=[toy_story,avatar,me_before_you,coco,frozen,gifted]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(frozen.VALID_RATINGS)
print(frozen.__doc__)
print(media.Movie.__name__)
print(frozen.__module__)
