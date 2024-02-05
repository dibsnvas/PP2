def get_ratings(name):
    for movie in movies:
        if movie["name"] == name:
            if movie["imdb"] > 5.5:
                return True
            else:
                return False
