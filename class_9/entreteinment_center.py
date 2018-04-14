import media
import fresh_tomatoes

alien = media.Movie("Alien","A story of a boy and his toys that come to life",
                "https://www.planetadelibros.com/usuaris/libros/fotos/68/original/alien_9788448005849.jpg",
                "https://www.youtube.com/watch?v=vwyZH85NQC4")

predator = media.Movie("Predator","A story of a boy and his toys that come to life",
                "http://es.web.img3.acsta.net/r_1920_1080/medias/nmedia/18/78/65/69/20070936.jpg",
                "https://www.youtube.com/watch?v=vwyZH85NQC4")

terminator = media.Movie("Terminator","A story of a boy and his toys that come to life",
                "https://vignette.wikia.nocookie.net/terminator/images/d/d0/Terminator_Cartel.jpg/revision/latest/scale-to-width-down/1000?cb=20150714111825&path-prefix=es",
                "https://www.youtube.com/watch?v=vwyZH85NQC4")

star_wars = media.Movie("Star Wars","A story of a boy and his toys that come to life",
                "https://www.revistaesfinge.com/media/k2/items/cache/2ff2ba0051687eef5ca0459cf942940c_XL.jpg",
                "https://www.youtube.com/watch?v=vwyZH85NQC4")

back_to_future = media.Movie("Back to the Future","A story of a boy and his toys that come to life",
                "https://ia.media-imdb.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,643,1000_AL_.jpg",
                "https://www.youtube.com/watch?v=vwyZH85NQC4")

transformers = media.Movie("Transformers","A story of a boy and his toys that come to life",
                "https://is1-ssl.mzstatic.com/image/thumb/Video128/v4/6c/28/2d/6c282d17-3423-6493-1709-6915a9686ef8/source/1200x630bb.jpg",
                "https://www.youtube.com/watch?v=vwyZH85NQC4")

movies = [alien,predator,terminator,star_wars,back_to_future,transformers]

#fresh_tomatoes.open_movies_page(movies)
print media.Movie.__module__