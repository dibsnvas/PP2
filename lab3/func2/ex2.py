def sublist_5_5():
    score_above_5_5 = []
    for m in movies:
        if m['imdb'] > 5.5:
            score_above_5_5.append(m['name'])
    return score_above_5_5

print(sublist_5_5())
