from sys import maxsize
movies_count = int(input())

max_rate = -maxsize
min_rate = maxsize
all_rates = 0

for movies in range(movies_count):
    movie_name = input()
    movie_rate = float(input())

    if movie_rate > max_rate:
        max_rate = movie_rate
        max_rate_movie = movie_name
    if movie_rate < min_rate:
        min_rate = movie_rate
        min_rate_movie = movie_name

    all_rates += movie_rate

middle_rate = all_rates / movies_count

print(f"{max_rate_movie} is with highest rating: {max_rate:.1f}")
print(f"{min_rate_movie} is with lowest rating: {min_rate:.1f}")
print(f'Average rating: {middle_rate:.1f}')