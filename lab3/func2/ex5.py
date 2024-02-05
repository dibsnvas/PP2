def category_computes_average(category):
    sum_category_movie = 0
    for m in movies:
        if m['category'] == category:
            sum_category_movie += m['imdb']
    return sum_category_movie/len(category_list(category))

print(category_computes_average('Romance'))
