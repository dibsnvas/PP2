def computes_average():
    sum = 0
    count = len(movies)
    for m in movies:
        sum += m['imdb']
    return sum/count

print(round(computes_average(), 2))
