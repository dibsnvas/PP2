def category_list(category):
    category_movie = []
    for m in movies:
        if m['category'] == category:
            category_movie.append(m['name'])
    return category_movie

print(category_list('Romance'))
